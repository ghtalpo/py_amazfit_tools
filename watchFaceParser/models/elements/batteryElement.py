import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._percent = None
        self._scale = None
        self._images = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getText(self):
        return self._text


    def getPercent(self):
        return self._percent


    def getScale(self):
        return self._scale


    def getImages(self):
        return self._images


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            from watchFaceParser.models.elements.battery.batteryNumberElement import BatteryNumberElement
            self._text = BatteryNumberElement(parameter = parameter, parent = self, name = '?_text?')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.elements.battery.batteryGaugeElement import BatteryGaugeElement # temp.
            self._images = BatteryGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images
        elif parameterId == 6:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._percent = ImageElement(parameter = parameter, parent = self, name = '?_percent?')
            return self._percent
        elif parameterId == 7:
            from watchFaceParser.models.elements.battery.circularBatteryElement import CircularBatteryElement
            self._scale = CircularBatteryElement(parameter = parameter, parent = self, name = '_scale')
            return self._scale
        else:
            return super(BatteryElement, self).createChildForParameter(parameter)

