import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.integerConverter import uint2int


class TemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._current = None
        self._symbols = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getCurrent(self):
        return self._current


    def getToday(self):
        return self._today


    def getSymbols(self):
        return self._symbols


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        images = []

        temperature = state.getCurrentTemperature()
        if not temperature:
            if self.getSymbols().getNoDataImageIndex():
                images.append(resources[self.getSymbols().getNoDataImageIndex()])
        else:
            temperature = int(temperature)
            if temperature < 0:
                temperature = -temperature
                if self.getSymbols().getMinusImageIndex():
                    images.append(resources[self.getSymbols().getMinusImageIndex()])

            if self.getCurrent():
                images.extend(self.getCurrent().getImagesForNumber(resources, temperature))

            if self.getSymbols():
                if self.getSymbols().getDegreesImageIndex():
                    images.append(resources[self.getSymbols().getDegreesImageIndex()])

        if self.getCurrent():
            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, images, uint2int(self.getCurrent().getSpacing()), self.getCurrent().getAlignment(), self.getCurrent().getBox())

        if self.getToday():
            self.getToday().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._current = NumberElement(parameter, self, '?_current?')
            return self._current
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.todayElement import TodayElement
            self._today = TodayElement(parameter = parameter, parent = self, name = 'Today')
            return self._today
        elif parameterId == 3:
            from watchFaceParser.models.elements.weather.symbolsElement import SymbolsElement
            self._symbols = SymbolsElement(parameter, self, '?_symbols?')
            return self._symbols
        else:
            super(TemperatureElement, self).createChildForParameter(parameter)

