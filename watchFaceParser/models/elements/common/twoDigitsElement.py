import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class TwoDigitsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._tens = None
        self._ones = None
        super(TwoDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getTens(self):
        return self._tens


    def getOnes(self):
        return self._ones


    def draw3(self, drawer, images, number):
        assert(type(images) == list)
        assert(type(number) == int)
        if number > 99:
            number = number % 100

        if self.getTens():
            self.getTens().draw3(drawer, images, int(number / 10))
        if self.getOnes():
            self.getOnes().draw3(drawer, images, int(number % 10))


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._tens = ImageSetElement(parameter, self, 'Tens')
            return self._tens
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._ones = ImageSetElement(parameter, self, 'Ones')
            return self._ones
        else:
            super(TwoDigitsElement, self).createChildForParameter(parameter)
