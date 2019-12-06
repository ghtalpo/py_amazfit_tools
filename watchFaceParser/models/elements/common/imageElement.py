import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config
from watchFaceParser.utils.integerConverter import uint2int


class ImageElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        super(ImageElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImageIndex(self):
        return self._imageIndex


    def setImageIndex(self, imageIndex):
        self._imageIndex = imageIndex


    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)


    def draw2x(self, drawer, images, angle, center):
        x = self._x
        y = self._y
        if angle is None:
            temp = images[self._imageIndex].getBitmap()
            drawer.paste(temp, (center.getX() + x, center.getY() + y), temp)
        else:
            bitmap = images[self._imageIndex].getBitmap()
            from PIL import Image
            # temp = Image.new('RGBA', (360, 360))
            # temp.paste(bitmap, (180 - x, 180 - y), bitmap)
            temp = Image.new('RGBA', (Config.getImageSize(), Config.getImageSize()))
            temp.paste(bitmap, (Config.getImageSizeHalf() - x, Config.getImageSizeHalf() - y), bitmap)
            temp = temp.rotate(angle)
            drawer.paste(temp, (center.getX() + 0, center.getY() + 0), temp)


    def draw2(self, drawer, images, angle):
        x = self._x
        y = self._y
        if angle is None:
            temp = images[self._imageIndex].getBitmap()
            drawer.paste(temp, (x,y), temp)
        else:
            bitmap = images[self._imageIndex].getBitmap()
            from PIL import Image
            # temp = Image.new('RGBA', (360, 360))
            # temp.paste(bitmap, (180 - x, 180 - y), bitmap)
            temp = Image.new('RGBA', (Config.getImageSize(), Config.getImageSize()))
            temp.paste(bitmap, (Config.getImageSizeHalf() - x, Config.getImageSizeHalf() - y), bitmap)
            temp = temp.rotate(angle)
            drawer.paste(temp, (0,0), temp)


    def createChildForParameter(self, parameter):
        if parameter.getId() == 3:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        else:
            super(ImageElement, self).createChildForParameter(parameter)
