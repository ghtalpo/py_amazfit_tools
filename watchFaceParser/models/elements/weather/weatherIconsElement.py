import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.weatherCondition import WeatherCondition


class WeatherIconsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._current = None
        self._customIcon = None
        self._currentAlt = None
        self._unknown4 = None
        super(WeatherIconsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getCurrent(self):
        return self._current

    def getCustomIcon(self):
        return self._customIcon

    def getCurrentAlt(self):
        return self._currentAlt

    def getUnknown4(self):
        return self._unknown4

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        logging.debug(f"[WeatherIconsElement]draw3 weather:{state.getCurrentWeather()}")

        useAltCoordinates = self.getCurrentAlt() is not None and state.CurrentTemperature is None
        iconCoordinates = self.getCurrentAlt() if useAltCoordinates else self.getCurrent()

        if state.getCurrentWeather() > WeatherCondition.VeryHeavyDownpour or state.getCurrentWeather() < WeatherCondition.Unknown:
            return

        if iconCoordinates is not None:
            # drawer.DrawImage(self.LoadWeatherImage(state.getCurrentWeather()), iconCoordinates.getX(), iconCoordinates.getY())
            temp = self.LoadWeatherImage(state.getCurrentWeather()).getBitmap()
            drawer.paste(temp, (iconCoordinates.getX(), iconCoordinates.getY()), temp)
            logging.debug(f"[WeatherIconsElement]draw3 weather:{state.getCurrentWeather()} icon draws!")


        if self.getCustomIcon() is not None:
            # drawer.DrawImage(resources[self.getCustomIcon().getImageIndex() + int(state.getCurrentWeather())], self.getCustomIcon().getX(), self.getCustomIcon().getY())
            temp = resources[self.getCustomIcon().getImageIndex() + int(state.getCurrentWeather())].getBitmap()
            drawer.paste(temp, (self.getCustomIcon().getX(), self.getCustomIcon().getY()), temp)
            logging.debug(f"[WeatherIconsElement]draw3 weather:{state.getCurrentWeather()} custom icon draws!")


    def LoadWeatherImage(weather):
        # var assembly = Assembly.GetExecutingAssembly();
        # var imageStream = assembly.GetManifestResourceStream($"WatchFace.Parser.WeatherIcons.{(int) weather}.png");
        # return (Bitmap) Image.FromStream(imageStream);
        from PIL import Image
        return Image.open(f"WatchFace.Parser.WeatherIcons.{int(weather)}.png")


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._number = CoordinatesElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._customIcon = ImageSetElement(parameter, self, 'CustomIcon')
            return self._customIcon
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._currentAlt = CoordinatesElement(parameter, self, 'CurrentAlt')
            return self._currentAlt
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._unknown4 = CoordinatesElement(parameter, self, 'Unkown4')
            return self._unknown4
        else:
            super(WeatherIconsElement, self).createChildForParameter(parameter)
