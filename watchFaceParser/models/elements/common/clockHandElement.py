import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class ClockHandElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._onlyBorder = False
        self._color = None
        self._center = None
        self._shape = []
        self._centerImage = None
        super(ClockHandElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getOnlyBorder(self):
        return self._onlyBorder


    def getColor(self):
        return self._color


    def getCenter(self):
        return self._center


    def getShape(self):
        return self._shape


    def getCenterImage(self):
        return self._centerImage


    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)

        if self.getCenterImage():
            angle = 360 - int(value * 360. / total)
            self.getCenterImage().draw2x(drawer, resources, angle, self.getCenter())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 5:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._centerImage = ImageElement(parameter = parameter, parent = self, name = 'CenterImage')
            return self._centerImage
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._center = CoordinatesElement(parameter = parameter, parent = self, name = 'CenterOffset')
            return self._center
        else:
            return super(ClockHandElement, self).createChildForParameter(parameter)

