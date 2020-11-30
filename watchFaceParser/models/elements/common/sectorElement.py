import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SectorElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._startAngle = None
        self._endAngle = None
        super(SectorElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getStartAngle(self):
        return self._startAngle


    def getEndAngle(self):
        return self._endAngle


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?startAngle?')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?endAngle?')
        else:
            super(SectorElement, self).createChildForParameter(parameter)
