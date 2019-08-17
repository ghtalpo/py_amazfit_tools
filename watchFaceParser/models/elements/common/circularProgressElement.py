import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement


class CircularProgressElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._radiusX = None
        self._radiusY = None
        self._startAngle = None
        self._endAngle = None
        self._width = None
        self._color = None
        self._unknown9 = None
        super(CircularProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getRadiusX(self):
        return self._radiusX


    def getRadiusY(self):
        return self._radiusY


    def getStartAngle(self):
        return self._startAngle


    def getEndAngle(self):
        return self._endAngle


    def getWidth(self):
        return self._width


    def getColor(self):
        return self._color


    def getUnknown9(self):
        return self._unknown9


    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)
        assert(type(value) == int)
        assert(type(total) == int)
        if value > total:
            value = total
        sectorAngle = int(1.0 * (self.getEndAngle() - self.getStartAngle()) * value / total)

        from PIL import ImageDraw
        d = ImageDraw.Draw(drawer) # draw context
        radius = self.getRadiusX()
        rect = (int(self.getX() - radius), int(self.getY() - radius),
            int(self.getX() + radius), int(self.getY() + radius))
        d.arc(rect, start = -90, end = -90 + sectorAngle, fill = self.getColor(), width = self.getWidth())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._radiusX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_radiusX?')
        elif parameterId == 4:
            self._radiusY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_radiusY?')
        elif parameterId == 5:
            self._startAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_startAngle?')
        elif parameterId == 6:
            self._endAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_endAngle?')
        elif parameterId == 7:
            self._width = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_width?')
        elif parameterId == 8:
            from resources.image.color import Color
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = '?_color?')
        elif parameterId == 9:
            self._unknown9 = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_unknown9?')
        else:
            return super(CircularProgressElement, self).createChildForParameter(parameter)
