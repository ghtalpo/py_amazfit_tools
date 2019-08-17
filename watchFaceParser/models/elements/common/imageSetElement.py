import logging
from watchFaceParser.models.elements.common.imageElement import ImageElement


class ImageSetElement(ImageElement):
    def __init__(self, parameter, parent, name = None):
        self._imagesCount = None
        super(ImageSetElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImagesCount(self):
        return self._imagesCount


    def draw3(self, drawer, resources, index):
        assert(type(resources) == list)
        assert(type(index) == int)
        if index >= self.getImagesCount():
            index = int(self.getImagesCount()) - 1
        imageIndex = int(self.getImageIndex() + index)
        temp = resources[imageIndex].getBitmap()
        drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        if parameter.getId() == 4:
            self._imagesCount = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?_imagesCount?')
        else:
            super(ImageSetElement, self).createChildForParameter(parameter)

