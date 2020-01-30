import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SeparateYearElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._year = None
        super(SeparateYearElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getYear(self):
        return self._year

    
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self.getYear():
            self.getYear().draw4(drawer, resources, state.getTime().year, 1)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._year = NumberElement(parameter = parameter, parent = self, name = 'Month')
            return self._year
        else:
            return super(SeparateYearElement, self).createChildForParameter(parameter)
