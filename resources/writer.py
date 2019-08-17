import logging
import io

import resources.image.reader
import resources.models.image


class Writer:
    OffsetTableItemLength = 4
    def __init__(self, stream):
        self._stream = stream


    def write(self, resources):
        assert(type(resources) == list)
        offsetsTableLength = len(resources) * self.OffsetTableItemLength
        offsetsTable = bytearray(offsetsTableLength)
        for i in range(offsetsTableLength):
            offsetsTable[i] = 0
        encodedResources = []

        cur_pos = self._stream.tell()
        num_padding = 4 - cur_pos % 4
        offset = num_padding

        for i in range(len(resources)):
            logging.debug(f"Resource {i} offset is {offset}...")
            offsetBytes = offset.to_bytes(4, byteorder='little')
            offsetsTable[i * self.OffsetTableItemLength:i * self.OffsetTableItemLength + 4] = offsetBytes

            encodedImage = io.BytesIO()
            logging.debug(f"Encoding resource {i}...")
            resources[i].writeTo(encodedImage)
            offset += len(encodedImage.getbuffer())
            encodedResources.append(encodedImage)

        logging.debug("Writing resources offsets table")
        self._stream.write(offsetsTable)

        logging.debug("Writing padding...")
        for i in range(num_padding):
            self._stream.write(int(0xff).to_bytes(1, byteorder='little'))

        logging.debug("Writing resources")
        for encodedImage in encodedResources:
            encodedImage.seek(0, 0)
            self._stream.write(encodedImage.read())
