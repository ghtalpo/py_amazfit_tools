import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class BackgroundElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        super(BackgroundElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getImage(self):
        return self._image


    def getFrontImage(self):
        return self._frontImage


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter = parameter, parent = self, name = 'Image')
            return self._image
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._frontImage = ImageElement(parameter = parameter, parent = self, name = 'FrontImage')
            return self._frontImage
        else:
            return super(BackgroundElement, self).createChildForParameter(parameter)