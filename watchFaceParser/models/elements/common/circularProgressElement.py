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
        self._flatness = None
        self._imageIndex = None
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


    def getFlatness(self):
        return self._flatness # TODO: works on real watch. no effects on previews.


    def getImageIndex(self):
        return self._imageIndex


    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)
        assert(type(value) == int)
        assert(type(total) == int)
        if value > total:
            value = total
        sectorAngle = int(1.0 * (self.getEndAngle() - self.getStartAngle()) * value / total)

        startAngle = -90 + self.getStartAngle()
        endAngle = -90 + self.getStartAngle() + sectorAngle

        if sectorAngle < 0:
            startAngle, endAngle = endAngle, startAngle

        if self._imageIndex:
            temp = resources[self._imageIndex].getBitmap()
            from PIL import Image
            #mask = Image.new('RGBA',temp.size,self.getColor())
            mask = Image.new('RGBA',temp.size,(0,0,0,0))

            from PIL import ImageDraw
            d = ImageDraw.Draw(mask) # draw context
            radius = self.getRadiusX() + int(self.getWidth() / 2) # patch for PIL arc

            rect = (0, 0,
                int((radius  )*2) , int((radius )*2))

            d.arc(rect, start = -90 + self.getStartAngle(), end = -90 + self.getStartAngle() + sectorAngle, fill = self.getColor(), width = self.getWidth())

            if self._flatness == 0:
                #round edges
                import math
                x = int(temp.size[0] / 2 + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y = int(temp.size[1] / 2 + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle() - 90)/180))
                d.ellipse((x- self.getWidth() / 2+1, y- self.getWidth() / 2+1, x+self.getWidth()/2-1, y+self.getWidth()/2-1), fill = self.getColor())

                x = int(temp.size[0] / 2 + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y = int(temp.size[1] / 2 + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                d.ellipse((x- self.getWidth() / 2+1, y- self.getWidth() / 2+1, x+self.getWidth()/2-1, y+self.getWidth()/2-1), fill = self.getColor())
            elif self._flatness == 90:
                #spike
                import math
                x1 = int(temp.size[0] / 2 + (radius - self.getWidth()) *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y1 = int(temp.size[1] / 2 + (radius - self.getWidth()) *math.sin(math.pi * (self.getStartAngle() - 90)/180))

                x2 = int(temp.size[0] / 2 + radius *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y2 = int(temp.size[1] / 2 + radius *math.sin(math.pi * (self.getStartAngle() - 90)/180))

                x3 = int(temp.size[0] / 2 + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle() -self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2)) - 90)/180))
                y3 = int(temp.size[1] / 2 + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle() -self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self.getColor())

                x1 = int(temp.size[0] / 2 + (radius - self.getWidth()) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y1 = int(temp.size[1] / 2 + (radius - self.getWidth()) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))

                x2 = int(temp.size[0] / 2 + radius *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y2 = int(temp.size[1] / 2 + radius *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))

                x3 = int(temp.size[0] / 2 + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle +self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2)) - 90)/180))
                y3 = int(temp.size[1] / 2 + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle +self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self.getColor())
            elif self._flatness == 180:
                pass
            drawer.paste(temp, (self.getX() - self.getRadiusX() - int(self._width  / 2), self.getY() - self.getRadiusY() - int(self._width  / 2)), mask)

        else:
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer) # draw context
            radius = self.getRadiusX() + int(self.getWidth() / 2) # patch for PIL arc
            rect = (int(self.getX() - radius), int(self.getY() - radius),
                int(self.getX() + radius), int(self.getY() + radius))
            d.arc(rect, start = startAngle, end = endAngle, fill = self.getColor(), width = self.getWidth())

            if self._flatness == 0:
                #round edges
                import math
                x = int(self.getX() + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y = int(self.getY() + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle() - 90)/180))
                d.ellipse((x- self.getWidth() / 2+1, y- self.getWidth() / 2+1, x+self.getWidth()/2-1, y+self.getWidth()/2-1), fill = self.getColor())

                x = int(self.getX() + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y = int(self.getY() + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                d.ellipse((x- self.getWidth() / 2+1, y- self.getWidth() / 2+1, x+self.getWidth()/2-1, y+self.getWidth()/2-1), fill = self.getColor())
            elif self._flatness == 90:
                #spike
                import math
                x1 = int(self.getX() + (radius - self.getWidth()) *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y1 = int(self.getY() + (radius - self.getWidth()) *math.sin(math.pi * (self.getStartAngle() - 90)/180))

                x2 = int(self.getX() + radius *math.cos(math.pi * (self.getStartAngle() - 90)/180))
                y2 = int(self.getY() + radius *math.sin(math.pi * (self.getStartAngle() - 90)/180))

                x3 = int(self.getX() + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle() -self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2)) - 90)/180))
                y3 = int(self.getY() + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle() -self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self.getColor())

                x1 = int(self.getX() + (radius - self.getWidth()) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y1 = int(self.getY() + (radius - self.getWidth()) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))

                x2 = int(self.getX() + radius *math.cos(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))
                y2 = int(self.getY() + radius *math.sin(math.pi * (self.getStartAngle()+ sectorAngle - 90)/180))

                x3 = int(self.getX() + (radius - self.getWidth() / 2) *math.cos(math.pi * (self.getStartAngle()+ sectorAngle +self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2)) - 90)/180))
                y3 = int(self.getY() + (radius - self.getWidth() / 2) *math.sin(math.pi * (self.getStartAngle()+ sectorAngle +self.getWidth() * 360 / (2*math.pi * (radius - self.getWidth() / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self.getColor())
            elif self._flatness == 180:
                pass


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
            self._flatness = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = '?_flatness?')
        elif parameterId == 10:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        else:
            return super(CircularProgressElement, self).createChildForParameter(parameter)
