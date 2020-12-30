import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement

class BatteryLinearElement(IconSetElement):
    def __init__(self, parameter, parent, name = None):
        self._ar = []
        super(BatteryLinearElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def getCoordinatesArray(self):
        return self._ar

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        index = int(state.getBatteryLevel() * len(self._ar) / 100)
        if index > 0:
            index -= 1
        super(BatteryLinearElement, self).draw3(drawer, resources, index)

    def createChildForParameter(self, parameter):
        if parameter.getId() == 1:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameter.getId() == 2:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter = parameter, parent = self, name = 'CenterOffset')
            self._ar.append(self._coordinates)
        else:
            super(IconSetElement, self).createChildForParameter(parameter)
