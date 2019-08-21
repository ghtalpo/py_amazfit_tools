import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SwitchElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._coordiates = None
        self._imageIndexOn = None
        self._imageIndexOff = None
        super(SwitchElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def switchState(self, state):
        return None


    def getCoordinates(self):
        return self._coordiates


    def getImageIndexOn(self):
        return self._imageIndexOn


    def getImageIndexOff(self):
        return self._imageIndexOff


    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        imageIndex = self.getImageIndexOn() if self.switchState(state) else self.getImageIndexOff()
        if imageIndex is None:
            return
        temp = images[imageIndex].getBitmap()
        drawer.paste(temp, (self.getCoordinates().getX(), self.getCoordinates().getY()), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._coordiates = CoordinatesElement(parameter = parameter, parent = self, name = 'CoordinatesElement')
            return self._coordiates
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._imageIndexOn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexOn')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._imageIndexOff = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexOff')
        else:
            return super(SwitchElement, self).createChildForParameter(parameter)

