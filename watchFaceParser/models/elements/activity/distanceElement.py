import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class DistanceElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._suffixImageIndex = None
        self._decimalPointImageIndex = None
        super(DistanceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getNumber(self):
        return self._number

    def getSuffixImageIndex(self):
        return self._suffixImageIndex

    def getDecimalPointImageIndex(self):
        return self._decimalPointImageIndex

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        kilometers = int(state.getDistance() / 1000)
        decimals = int(state.getDistance() % 1000 / 10)

        images = self.getNumber().getImagesForNumber(resources, kilometers)
        images.append(resources[self.getDecimalPointImageIndex()])
        for image in self.getNumber().getImagesForNumber(resources, decimals):
            images.append(image)
        if self.getSuffixImageIndex():
            images.append(resources[self.getSuffixImageIndex()])

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, int(self.getNumber().getSpacing()), self.getNumber().getAlignment(), self.getNumber().getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._suffixImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._decimalPointImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'DecimalPointImageIndex')
        else:
            super(DistanceElement, self).createChildForParameter(parameter)
