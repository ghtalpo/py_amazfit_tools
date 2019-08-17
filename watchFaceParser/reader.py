import logging
import io

from watchFaceParser.models.parameter import Parameter


class Reader:
    def __init__(self, stream):
        self._stream = stream

    def getParameters(self):
        return self._parameters

    def read(self):
        logging.info("Reading header...")
        from watchFaceParser.models.header import Header
        header = Header.readFrom(self._stream)
        logging.info("Header was read:")
        logging.info(f"Signature: {header.signature}, Unknown: {header.unknown}, ParametersSize: {header.parametersSize}, isValid: {header.isValid()}")

        if not header.isValid():
            return

        logging.info("Reading parameter offsets...")
        tmpArray = bytearray(self._stream.read(header.parametersSize))
        parametersStream = io.BytesIO(tmpArray) 
        logging.info("Parameter offsets were read from file")

        logging.info("Reading parameters descriptor...")
        mainParam = Parameter.readFrom(parametersStream)
        logging.info("getParameters descriptor was read:")
        parametersTableLength = mainParam.getChildren()[0].getValue()
        imagesCount = mainParam.getChildren()[1].getValue()
        logging.info(f"ParametersTableLength: {parametersTableLength}, ImagesCount: {imagesCount}")

        logging.info("Reading parameters locations...")
        parametersLocations = Parameter.readList(parametersStream)
        logging.info("Watch face parameters locations were read:")

        self._parameters = self.readParameters(parametersTableLength, parametersLocations)
        from resources.reader import Reader
        self._resources = Reader(self._stream).read(imagesCount)


    def readParameters(self, coordinatesTableSize, parametersDescriptors):
        parametersStream = io.BytesIO(bytearray(self._stream.read(coordinatesTableSize)))

        result = []
        for parameterDescriptor in parametersDescriptors:
            descriptorOffset = parameterDescriptor.getChildren()[0].getValue()
            descriptorLength = parameterDescriptor.getChildren()[1].getValue()
            logging.info(f"Reading descriptor for parameter {parameterDescriptor.getId()}")
            logging.info(f"Descriptor offset: {descriptorOffset}, Descriptor length: {descriptorLength}")
            parametersStream.seek(descriptorOffset)
            descriptorStream = io.BytesIO(bytearray(parametersStream.read(descriptorLength)))
            logging.info(f"Parsing descriptor for parameter {parameterDescriptor.getId()}...")
            result.append(Parameter(parameterDescriptor.getId(), Parameter.readList(descriptorStream)))

        return result


    def getResources(self):
        return self._resources


    def getImages(self):
        from resources.models.image import Image
        t = []
        for resource in self._resources:
            if type(resource) == Image:
                t.append(resource)
        return t
