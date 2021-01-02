import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class Animation2Element(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._animation2 = None
        super(Animation2Element, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getAnimation2p1(self):
        return self._animation2p1


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.animation.animation2p1Element import Animation2p1Element
            self._animation2p1 = Animation2p1Element(parameter = parameter, parent = self, name = 'Animation2')
            return self._animation2p1
        else:
            return super(Animation2Element, self).createChildForParameter(parameter)