import logging
import io

from watchFaceParser.models.parameterFlags import ParameterFlags


def long2ulong(n):
    if type(n) == int:
        if n < 0:
            return 0xffffffffffffffff + n + 1
    return n


class Parameter:
    def __init__(self, _id, value):
        if type(value) == int:
            self._id = _id
            self._value = value
            self._children = None
        elif type(value) == list:
            self._id = _id
            self._value = None
            self._children = value
        else:
            raise Exception(f'invalid type for parameter {value}:{type(value)}')


    def getId(self):
        return self._id


    def getChildren(self):
        return self._children


    def getValue(self):
        return self._value


    def hasChildren(self):
        return self._children and len(self._children) > 0


    @staticmethod
    def writeByte(stream, v):
        stream.write(int(v).to_bytes(1, byteorder='little'))


    def write(self, stream, traceOffset = 0):
        assert(type(traceOffset) == int)
        size = 0
        flags = ParameterFlags.hasChildren if self.hasChildren() else 0
        rawId = 0xff & ((self.getId() << 3) + flags)
        Parameter.writeByte(stream, rawId)

        size += 1
        if self.hasChildren():
            logging.debug(("\t" * traceOffset) + f"{self.getId()} ({rawId:02X}):")
            size += self.writeList(stream, traceOffset + 1)
            logging.debug(("\t" * traceOffset) + f"{size} bytes")
            return size
        size += self.writeValue(stream, self.getValue(), traceOffset)
        logging.debug(("\t" * traceOffset) + f"{self.getId()} ({rawId:02X}): {self.getValue()} ({self.getValue():02X})")
        return size


    def writeList(self, stream, traceOffset):
        assert(type(traceOffset) == int)
        temporaryStream = io.BytesIO()
        for parameter in self.getChildren():
            parameter.write(temporaryStream, traceOffset)
        size = self.writeValue(stream, len(temporaryStream.getbuffer()), traceOffset)
        temporaryStream.seek(0, 0)
        stream.write(temporaryStream.read())
        size += len(temporaryStream.getbuffer())
        return size


    def writeValue(self, stream, value, traceOffset):
        assert(type(value) == int)
        assert(type(traceOffset) == int)
        unsignedValue = long2ulong(value)
        size = 0
        currentByte = 0
        while unsignedValue >= 0x80:
            currentByte = 0xff & ((unsignedValue & 0x7f) | 0x80)
            Parameter.writeByte(stream, currentByte)
            size += 1
            unsignedValue = unsignedValue >> 7

        currentByte = 0xff & (unsignedValue & 0x7f)
        Parameter.writeByte(stream, currentByte)
        size += 1
        return size


    @staticmethod
    def readList(stream, traceOffset = 0):
        result = []
        try:
            while True:
                parameter = Parameter.readFrom(stream, traceOffset)
                result.append(parameter)
        except EOFError:
            pass
        except IndexError:
            pass
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
        return result


    @staticmethod
    def readFrom(fileStream, traceOffset = 0):
        rawId = Parameter.readByte(fileStream, traceOffset)
        _id = (rawId & 0xf8) >> 3
        flags = ParameterFlags(rawId & 0x07)

        if _id == 0:
            raise IndexError("Parameter with zero Id is invalid.") #ArgumentException

        value = Parameter.readValue(fileStream, traceOffset)
        if flags.hasFlag(ParameterFlags.hasChildren):
            logging.info(Parameter.traceWithOffset(f"{_id} ({rawId:2X}): {value} bytes", traceOffset))
            buffer = fileStream.read(value)
            stream = io.BytesIO(buffer)

            _list = Parameter.readList(stream, traceOffset + 1)
            return Parameter(_id, _list)
        logging.info(Parameter.traceWithOffset(f"{_id} ({rawId:2X}): {value} {value:2X}", traceOffset))
        return Parameter(_id, value)


    @staticmethod
    def readValue(fileStream, traceOffset = 0):
        bytesLength = 0
        value = 0
        offset = 0

        currentByte = Parameter.readByte(fileStream, traceOffset)
        bytesLength = bytesLength + 1

        while (currentByte & 0x80) > 0:
            if bytesLength > 9:
                raise Exception("Value of the parameter too long")
            value = value | ((currentByte & 0x7f) << offset)
            offset += 7
            currentByte = Parameter.readByte(fileStream, traceOffset)
            bytesLength = bytesLength + 1

        value = value | ((currentByte & 0x7f) << offset)
        return value


    @staticmethod
    def readByte(stream, traceoffset = 0):
        currentByte = int.from_bytes(stream.read(1), byteorder='little')
        return currentByte


    @staticmethod
    def traceWithOffset(message, offset):
        return '    ' * offset + message
