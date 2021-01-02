import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class Animation2Element(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._animation2p1 = None
        self._animation2p2 = None
        super(Animation2Element, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getAnimation2p1(self):
        return self._animation2p1


    def getAnimation2p2(self):
        return self._animation2p2


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.animation.animation2p1Element import Animation2p1Element
            self._animation2p1 = Animation2p1Element(parameter = parameter, parent = self, name = 'Animation2p1')
            return self._animation2p1
        elif parameterId == 2:
            self._animation2p2 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = 'Animation2p2')
        else:
            return super(Animation2Element, self).createChildForParameter(parameter)