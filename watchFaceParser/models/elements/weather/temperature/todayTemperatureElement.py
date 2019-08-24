import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TodayTemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._separate = None
        self._oneline = None
        super(TodayTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getSeparate(self):
        return self._separate


    def getOneline(self):
        return self._oneline


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.temperature.today.separateTemperatureElement import SeparateTemperatureElement
            self._separate = SeparateTemperatureElement(parameter, self, 'Number')
            return self._separate
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperature.today.onelineTemperatureElement import OnelineTemperatureElement
            self._oneline = OnelineTemperatureElement(parameter, self, 'Number')
            return self._oneline
        else:
            super(TodayTemperatureElement, self).createChildForParameter(parameter)

