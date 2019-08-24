import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class TemperatureNumberElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._minusImageIndex = None
        self._degreesImageIndex = None
        super(TemperatureNumberElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getNumber(self):
        return self._number


    def getMinusImageIndex(self):
        return self._minusImageIndex


    def getDegreesImageIndex(self):
        return self._degreesImageIndex


    def draw4(self, drawer, resources, temperature, altCoordinates = None):
        assert(type(resources) == list)
        drawingBox = self.getNumber().getBox() if altCoordinates is None else self.getNumber().getAltBox(altCoordinates)
        images = self.getImagesForTemperature(resources, temperature)
        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, int(self.getNumber().getSpacing()), self.getNumber().getAlignment(), drawingBox)


    def getImagesForTemperature(self, resources, temperature):
        assert(type(resources) == list)
        images = []
        if temperature < 0:
            images.append(resources[self.getMinusImageIndex()])
        # images.AddRange(self.getNumber().GetImagesForNumber(resources, math.abs(temperature)))
        for image in self.getNumber().getImagesForNumber(resources, abs(temperature)):
            images.append(image)
        if self.getDegreesImageIndex():
            images.append(resources[self.getDegreesImageIndex()])
        return images


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._minusImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'MinusImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._degreesImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'DegreesImageIndex')
        else:
            super(TemperatureNumberElement, self).createChildForParameter(parameter)

