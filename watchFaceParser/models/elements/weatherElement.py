import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class WeatherElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._icon = None
        self._temperature = None
        super(WeatherElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getIcon(self):
        return self._icon


    def getTemperature(self):
        return self._temperature


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.weatherIconElement import WeatherIconElement
            self._icon = WeatherIconElement(parameter = parameter, parent = self, name = '?_icon?')
            return self._icon
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperatureElement import TemperatureElement # temp.
            self._temperature = TemperatureElement(parameter = parameter, parent = self, name = '?_temperature?')
            return self._temperature
        else:
            return super(WeatherElement, self).createChildForParameter(parameter)

