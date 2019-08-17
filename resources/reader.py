import logging
import io

class Reader:
    OffsetTableItemLength = 4
    def __init__(self, stream):
        self._stream = stream
        self._binaryReader = self._stream

    def read(self, resourcesCount):
        offsetsTableLength = resourcesCount * self.OffsetTableItemLength
        logging.info(f"Reading resources offsets table with {resourcesCount} elements ({offsetsTableLength} bytes)")

        offsets = []
        for i in range(resourcesCount):
            offset = int.from_bytes(self._binaryReader.read(4), byteorder='little')
            offsets.append(offset)

        resourcesOffset = self._stream.tell()
        self._stream.seek(0, 2); fileSize = self._stream.tell() ; self._stream.seek(resourcesOffset)

        resources = []
        for i in range(resourcesCount):
            offset = offsets[i] + resourcesOffset
            nextOffset = offsets[i+1] + resourcesOffset if i + 1 < resourcesCount else fileSize
            length = nextOffset - offset
            logging.info(f"Resource {i} offset: {offset}, length: {length}...")
            if self._stream.tell() != offset:
                bytesGap = offset - self._stream.tell()
                logging.warn(f"Found {bytesGap} bytes gap before resource number {i}")
                self._stream.seek(offset)

            logging.debug(f"Reading resource {i}...")
            try:
                from resources.image.reader import Reader
                from resources.models.image import Image

                bitmap = Reader(self._stream).read()
                image = Image(bitmap)
                resources.append(image)
            except TypeError: # InvalidResourceException
                logging.warn("Resource is not an image")
                raise

        return resources

