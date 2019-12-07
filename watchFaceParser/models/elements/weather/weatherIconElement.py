import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.weatherCondition import WeatherCondition


class WeatherIconElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._images = None
        self._noWeatherImageIndex = None
        super(WeatherIconElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getImages(self):
        return self._images


    def getNoWeatherImageIndex(self):
        return self._noWeatherImageIndex


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        if state.getCurrentWeather() > WeatherCondition.VeryHeavyDownpour or state.getCurrentWeather() < WeatherCondition.Unknown:
            if self.getImages():
                if self.getNoWeatherImageIndex():
                    temp = resources[self.getNoWeatherImageIndex()].getBitmap()
                    drawer.paste(temp, (self.getImages().getX(), self.getImages().getY()), temp)
            return

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        if self.getImages():
            self.getImages().draw3(drawer, resources, state.getCurrentWeather())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._images = ImageSetElement(parameter, self, '?_images?')
            return self._images
        elif parameterId == 2:
            self._noWeatherImageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_noWeatherImageIndex?')
        else:
            super(WeatherIconElement, self).createChildForParameter(parameter)
