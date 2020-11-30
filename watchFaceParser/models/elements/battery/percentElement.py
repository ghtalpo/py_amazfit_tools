import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class PercentElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        super(PercentElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getImageIndex(self):
        return self._imageIndex


    #def draw3(self, drawer, resources, state):
    #    assert(type(resources) == list)
    #    imageIndex = self.getImageIndexAmCn() if state.getTime().hour < 12 else self.getImageIndexPmCn()
    #    temp = resources[imageIndex].getBitmap()
    #    drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._imageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndex')
        else:
#            print ("PercentElement",parameterId)
            return super(PercentElement, self).createChildForParameter(parameter)

