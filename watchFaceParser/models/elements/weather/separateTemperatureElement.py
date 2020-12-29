import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class SeparateTemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._day = None
        self._night = None
        super(SeparateTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getDay(self):
        return self._day

    def getNight(self):
        return self._night

    def draw3(self, drawer, resources, state):
        symbols = self._parent._parent.getSymbols()
        # appendDegreesForBoth = self._parent.getAppendDegreesForBoth()

        if self.getDay():
            temperature = state.getDayTemperature()
            if temperature:
                images = []
                if temperature < 0:
                    temperature = -temperature
                    if symbols.getMinusImageIndex():
                        images.append(resources[symbols.getMinusImageIndex()])
                images.extend(self.getDay().getImagesForNumber(resources, temperature, 2))
                if symbols:
                    if symbols.getDegreesImageIndex():
                        images.append(resources[symbols.getDegreesImageIndex()])

                from watchFaceParser.helpers.drawerHelper import DrawerHelper
                DrawerHelper.drawImages(drawer, images, uint2int(self.getDay().getSpacing()), self.getDay().getAlignment(), self.getDay().getBox())

        if self.getNight():
            temperature = state.getNightTemperature()
            if temperature:
                images = []
                if temperature < 0:
                    temperature = -temperature
                    if symbols.getMinusImageIndex():
                        images.append(resources[symbols.getMinusImageIndex()])
                images.extend(self.getNight().getImagesForNumber(resources, temperature, 2))
                if symbols:
                    if symbols.getDegreesImageIndex():
                        images.append(resources[symbols.getDegreesImageIndex()])

                from watchFaceParser.helpers.drawerHelper import DrawerHelper
                DrawerHelper.drawImages(drawer, images, uint2int(self.getNight().getSpacing()), self.getNight().getAlignment(), self.getNight().getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter = parameter, parent = self, name = 'Day')
            return self._day
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._night = NumberElement(parameter = parameter, parent = self, name = 'Night')
            return self._night
        else:
            logging.debug ("Unknown SeparateTemperatureElement",parameterId)
            return super(SeparateTemperatureElement, self).createChildForParameter(parameter)
