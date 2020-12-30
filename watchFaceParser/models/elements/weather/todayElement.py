import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
#from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.utils.parametersConverter import uint2int


class TodayElement(CompositeElement):
#class TodayElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._separate = None
        self._current = None
        self._appendDegreesForBoth = None
        super(TodayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getAppendDegreesForBoth(self):
        return self._appendDegreesForBoth


    def getCurrent(self):
        return self._current


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        images = []

        if self.getCurrent():
            self.getCurrent().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            #separate
            from watchFaceParser.models.elements.weather.separateTemperatureElement import SeparateTemperatureElement
            self._current = SeparateTemperatureElement(parameter, self, '?_separate?')
            return self._current
        elif parameterId == 3:
            #AppendDegreesForBoth
            self._appendDegreesForBoth = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_appendDegreesForBoth?')
        else:
            logging.debug ("Unknown TodayElement", parameterId)
            super(TodayElement, self).createChildForParameter(parameter)

