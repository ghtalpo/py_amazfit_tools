import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SymbolsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._unknown0800 = None
        self._minusImageIndex = None
        self._degreesImageIndex = None
        self._noDataImageIndex = None
        super(SymbolsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getUnknown0800(self):
        return self._unknown0800


    def getMinusImageIndex(self):
        return self._minusImageIndex


    def getDegreesImageIndex(self):
        return self._degreesImageIndex


    def getNoDataImageIndex(self):
        return self._noDataImageIndex


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            self._unknown0800 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_unknown0800?')
        elif parameterId == 2:
            self._minusImageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_minusImageIndex?')
        elif parameterId == 3:
            self._degreesImageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_degreesImageIndex?')
        elif parameterId == 4:
            self._noDataImageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_noDataImageIndex?')
        else:
            super(SymbolsElement, self).createChildForParameter(parameter)

