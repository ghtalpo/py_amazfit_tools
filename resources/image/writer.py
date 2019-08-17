import logging


class Writer:
    signature = bytearray(b'BM\xff\xff')


    def __init__(self, stream):
        self._writer = stream


    def write(self, image):
        self._image = image
        self._width = image.size[0]
        self._height = image.size[1]

        self._bitsPerPixel = 32
        self._unknown1 = 24
        self._unknown2 = 1

        import math
        self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)

        self._writer.write(Writer.signature)

        self.writeHeader()
        self.writeImage()


    def writeHeader(self):
        logging.debug("Writing image header...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, Unknown1: {self._unknown1}, Unknown2: {self._unknown2}")

        self._writer.write(self._width.to_bytes(4, byteorder='little'))
        self._writer.write(self._height.to_bytes(4, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(4, byteorder='little'))
        self._writer.write(self._unknown1.to_bytes(4, byteorder='little'))
        self._writer.write(self._unknown2.to_bytes(4, byteorder='little'))


    def writeImage(self):
        logging.debug("Writing image...")

        pixels = self._image.convert('RGBA')
        data = pixels.getdata()

        for pixel in data:
            (r, g, b, a) = pixel
            self._writer.write(b.to_bytes(1, byteorder='little'))
            self._writer.write(g.to_bytes(1, byteorder='little'))
            self._writer.write(r.to_bytes(1, byteorder='little'))
            self._writer.write(a.to_bytes(1, byteorder='little'))
