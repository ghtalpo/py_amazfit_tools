import logging

from watchFaceParser.models.elements.weather.temperature.temperatureNumberElement import TemperatureNumberElement


class CurrentTemperatureElement(TemperatureNumberElement):
    def __init__(self, parameter, parent = None, name = None):
        super(CurrentTemperatureElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getCurrentTemperature():
            super(CurrentTemperatureElement, self).draw4(drawer, resources, state.getCurrentTemperature())