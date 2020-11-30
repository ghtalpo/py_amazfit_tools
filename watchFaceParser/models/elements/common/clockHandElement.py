import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class ClockHandElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._onlyBorder = False
        self._color = None
        self._center = None
        self._shape = []
        self._sector = []
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

    def getSector(self):
        return self._sector

    def getCenterImage(self):
        return self._centerImage


    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)

        _startAngle = 0
        _endAngle = 360
        if self.getSector():
            if self.getSector().getStartAngle():
                _startAngle = self.getSector().getStartAngle() / 100
            if self.getSector().getEndAngle():
                _endAngle = self.getSector().getEndAngle() / 100

        if self.getCenterImage():
            angle = 360 - _startAngle - int(value * (_endAngle - _startAngle ) / (total-1))
            self.getCenterImage().draw2x(drawer, resources, angle, self.getCenter())
#360 - (10 * 225 / 150)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            #from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            #self._center = CoordinatesElement(parameter = parameter, parent = self, name = 'OnlyBorder')
            #return self._center
            pass
        elif parameterId == 2:
            from resources.image.color import Color
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = '?_color?')
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._center = CoordinatesElement(parameter = parameter, parent = self, name = 'CenterOffset')
            return self._center
        if parameterId == 4:
            #from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            #self._center = CoordinatesElement(parameter = parameter, parent = self, name = 'Shape')
            #return self._center
            pass
        elif parameterId == 5:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._centerImage = ImageElement(parameter = parameter, parent = self, name = 'Image')
            return self._centerImage
        elif parameterId == 6:
            from watchFaceParser.models.elements.common.sectorElement import SectorElement
            self._sector = SectorElement(parameter = parameter, parent = self, name = 'Sector')
            return self._sector
            pass
        else:
            return super(ClockHandElement, self).createChildForParameter(parameter)

