from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
import logging


class PmElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._x2 = None
        self._y2 = None
        self._x3 = None
        super(PmElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getX2(self):
        return self._x2


    def getY2(self):
        return self._y2


    def getX3(self):
        return self._x3


    # def draw3(self, drawer, resources, state):
    #     assert(type(resources) == list)
    #     imageIndex = self.getImageIndexAmCn() if state.getTime().hour < 12 else self.getImageIndexPmCn()
    #     temp = resources[imageIndex].getBitmap()
    #     drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._x2 = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'X2')
        elif parameterId == 4:
            self._y2 = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Y2')
        elif parameterId == 5:
            self._x3 = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'X3')
        else:
            return super(PmElement, self).createChildForParameter(parameter)

