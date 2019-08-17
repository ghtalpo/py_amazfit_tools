import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class CoordinatesElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = None
        self._y = None
        super(CoordinatesElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._x = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?X?')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._y = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?Y?')
        else:
            super(CoordinatesElement, self).createChildForParameter(parameter)
