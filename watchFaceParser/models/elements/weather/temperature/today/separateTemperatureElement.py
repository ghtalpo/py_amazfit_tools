import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class SeparateTemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._day = None
        self._night = None
        self._dayAlt = None
        self._nightAlt = None
        super(SeparateTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getDay(self):
        return self._day


    def getNight(self):
        return self._night


    def getDayAlt(self):
        return self._dayAlt


    def getNightAlt(self):
        return self._nightAlt


    def draw3(self, drawer, images, state):
        assert(type(images) == list)
        if state.getCurrentTemperature():
            if state.getDayTemperature() and self.getDay():
                self.getDay().draw4(drawer, images, state.getDayTemperature())
            if state.getNightTemperature() and self.getNight():
                self.getNight().draw4(drawer, images, state.getNightTemperature())
        else:
            if state.getDayTemperature() and self.getDay():
                self.getDay().draw4(drawer, images, state.getDayTemperature(), self.getDayAlt())
            if state.getNightTemperature() and self.getNight():
                self.getNight().draw4(drawer, images, state.getNightTemperature(), self.getNightAlt())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.temperature.temperatureNumberElement import TemperatureNumberElement
            self._day = TemperatureNumberElement(parameter, self, 'Day')
            return self._day
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperature.temperatureNumberElement import TemperatureNumberElement
            self._night = TemperatureNumberElement(parameter, self, 'Night')
            return self._night
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._dayAlt = CoordinatesElement(parameter, self, 'DayAlt')
            return self._dayAlt
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._nightAlt = CoordinatesElement(parameter, self, 'NightAlt')
            return self._nightAlt
        else:
            super(SeparateTemperatureElement, self).createChildForParameter(parameter)

