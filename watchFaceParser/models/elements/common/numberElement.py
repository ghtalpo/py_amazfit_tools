import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class Box:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def getWidth(self):
        return self._width


    def getHeight(self):
        return self._height


    def getLeft(self):
        return self._x


    def getRight(self):
        return self._x + self._width


    def getTop(self):
        return self._y


    def getBottom(self):
        return self._y + self._height


class NumberElement(CoordinatesElement):
    def __init__(self, parameter, parent, name):
        self._bottomRightX = None
        self._bottomRightY = None
        self._alignment = None
        self._spacing = None
        self._imageIndex = None
        self._imagesCount = None
        super(NumberElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getBottomRightX(self):
        return self._bottomRightX


    def getBottomRightY(self):
        return self._bottomRightY


    def getAlignment(self):
        return self._alignment


    def getSpacing(self):
        return self._spacing


    def getImageIndex(self):
        return self._imageIndex


    def getImagesCount(self):
        return self._imagesCount


    def getBox(self):
        return Box(self._x, self._y, self._bottomRightX - self._x, self._bottomRightY - self._y)


    def getAltBox(self, altCoordinates):
        return Box(altCoordinates._x, altCoordinates._y, self._bottomRightX - self._x, self._bottomRightY - self._y)


    def draw4(self, drawer, images, number, minimumDights = 1):
        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, self.getImagesForNumber(images, number, minimumDights), self._spacing, self._alignment, self.getBox())


    def getImagesForNumber(self, images, number, minimumDigits = 1):
        stringNumber = str(number).zfill(minimumDigits)
        return [images[self._imageIndex + int(digit)] for digit in stringNumber if int(digit) < self._imagesCount]


    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()

        if parameterId == 3:
            self._bottomRightX = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightX')
        elif parameterId == 4:
            self._bottomRightY = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightY')
        elif parameterId == 5:
            self._alignment = parameter.getValue()
            return ValueElement(parameter, self, 'Alignment')
        elif parameterId == 6:
            self._spacing = parameter.getValue()
            return ValueElement(parameter, self, 'Spacing')
        elif parameterId == 7:
            self._imageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 8:
            self._imagesCount = parameter.getValue()
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(NumberElement, self).createChildForParameter(parameter)

