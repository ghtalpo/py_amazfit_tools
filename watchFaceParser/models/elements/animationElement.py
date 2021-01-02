import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AnimationElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._animation2 = None
        super(AnimationElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getAnimation2(self):
        return self._animation2


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 2:
            from watchFaceParser.models.elements.animation.animation2Element import Animation2Element
            self._animation2 = Animation2Element(parameter = parameter, parent = self, name = 'Animation2')
            return self._animation2
        else:
            return super(AnimationElement, self).createChildForParameter(parameter)