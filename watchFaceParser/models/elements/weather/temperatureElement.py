import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._current = None
        self._today = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getCurrent(self):
        return self._current


    def getToday(self):
        return self._today


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.temperature.currentTemperatureElement import CurrentTemperatureElement
            self._current = CurrentTemperatureElement(parameter, self, 'Number')
            return self._current
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperature.todayTemperatureElement import TodayTemperatureElement
            self._today = TodayTemperatureElement(parameter, self, 'CustomIcon')
            return self._today
        else:
            super(TemperatureElement, self).createChildForParameter(parameter)
