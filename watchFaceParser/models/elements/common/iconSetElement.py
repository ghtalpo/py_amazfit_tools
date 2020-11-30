import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config


class IconSetElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        self._coordinates = None
        super(IconSetElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImageIndex(self):
        return self._imageIndex


    def setImageIndex(self, imageIndex):
        self._imageIndex = imageIndex


    def draw3(self, drawer, resources, state, cursor = None):
        #print ("IconSetElement",self)
        self.draw2(drawer, resources, state, cursor)


    def draw2(self, drawer, images, state = None, cursor = None):
        #print("getCoorArray",self.getCoordinatesArray(),self._imageIndex,len( self.getCoordinatesArray()),state)
        initial = 0
        if cursor == True:
            initial = state
        for i in range(initial, state + 1):
            x = self.getCoordinatesArray()[i]._x
            y = self.getCoordinatesArray()[i]._y
            temp = images[self._imageIndex + i].getBitmap()
            #print (temp, x, y, state)
            drawer.paste(temp, (x,y), temp)


#    def createChildForParameter(self, parameter):
#        #elif parameter.getId() == 2:
#        #    from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
#            #print ( parameter.getValue(),parameter.getChildren())
#            #print (self.getName(),[c.getValue() for c in parameter.getChildren()])
#            #self._coordinates = [ CoordinatesElement(parameter = c, parent = self, name = 'CenterOffset') for c in parameter.getChildren()]
#            #self._coordinates = CoordinatesElement(parameter = parameter.getChildren(), parent = self, name = 'CenterOffset')
#            #return self._coordinates
#
#        else:
#            print ("unknown",parameter.getId())
#            super(IconSetElement, self).createChildForParameter(parameter)
#