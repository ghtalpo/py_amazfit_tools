import logging
import io
from PIL import Image

import resources.image.color


class Reader():
    def __init__(self, stream):
        self._reader = stream
        self._bip = True


    def read(self):
        signature = self._reader.read(4)
        if signature[0] != ord('B') or signature[1] != ord('M'):
            print(signature)
            raise TypeError("Image signature doesn't match.")

        if signature[2] == 0xff and signature[2] == 0xff:
            logging.warn("The image is 32bit.")
            self._bip = False

        if self._bip:
            assert(False) # not implemented
        else:
            self.readHeader()
            return self.readImage()


    def readImage(self):
        image = Image.new('RGBA', (self._width, self._height))
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                b = rowBytes[x * self._step]
                g = rowBytes[x * self._step + 1]
                r = rowBytes[x * self._step + 2]
                if self._step == 4:
                    alpha = rowBytes[x * self._step + 3]
                else:
                    alpha = 255
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                image.putpixel((x,y), color)
        return image


    def readHeader(self):
        logging.info("Reading image header(non-bip)...")
        self._width = int.from_bytes(self._reader.read(4), byteorder='little')
        self._height = int.from_bytes(self._reader.read(4), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(4), byteorder='little')
        self._unknown1 = int.from_bytes(self._reader.read(4), byteorder='little')
        self._unknown2 = int.from_bytes(self._reader.read(4), byteorder='little')
        self._step = int(self._bitsPerPixel / 8)
        self._rowLengthInBytes = self._width * self._step
        self._transparency = False
        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"BPP: {self._bitsPerPixel}, Transparency: {self._transparency}")

