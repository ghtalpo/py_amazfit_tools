from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
import logging


class AmPmElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndexAmCn = None
        self._imageIndexPmCn = None
        super(AmPmElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImageIndexAmCn(self):
        return self._imageIndexAmCn


    def getImageIndexPmCn(self):
        return self._imageIndexPmCn


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        imageIndex = self.getImageIndexAmCn() if state.getTime().hour < 12 else self.getImageIndexPmCn()
        temp = resources[imageIndex].getBitmap()
        drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._imageIndexAmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexAmCn')
        elif parameterId == 4:
            self._imageIndexPmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexPmCn')
        else:
            return super(AmPmElement, self).createChildForParameter(parameter)

