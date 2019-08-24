import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class WeatherElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._weatherIcons = None
        self._temperature = None
        super(WeatherElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getWeatherIcons(self):
        return self._weatherIcons


    def getTemperature(self):
        return self._temperature


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.weatherIconsElement import WeatherIconsElement
            self._weatherIcons = WeatherIconsElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._weatherIcons
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperatureElement import TemperatureElement
            self._temperature = TemperatureElement(parameter = parameter, parent = self, name = 'WeekDay')
            return self._temperature
        else:
            return super(WeatherElement, self).createChildForParameter(parameter)
