from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class DistanceElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        super(DistanceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getNumber(self):
        return self._number

    def getKilometerImageIndex(self):
        return self._kilometerImageIndex

    def getDecimalPointImageIndex(self):
        return self._decimalPointImageIndex

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        kilometers = state.getDistance() / 1000
        decimals = state.getDistance() % 1000 / 10

        images = self.getNumber().getImagesForNumber(resources, kilometers)
        images.append(resources[self.getDecimalPointImageIndex()])
        for image in self.getNumber().getImagesForNumber(resources, decimals):
            images.add(image)
        images.append(resources[self.getKilometerImageIndex()])

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, int(self.getNumber().Spacing), self.getNumber().Alignment, self.getNumber().GetBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._kilometerImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'KilometerImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._decimalPointImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'DecimalPointImageIndex')
        else:
            super(DistanceElement, self).createChildForParameter(parameter)
