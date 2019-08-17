import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._steps = None
        self._pulse = None
        self._circleRange = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getSteps(self):
        return self._steps


    def getPulse(self):
        return self._pulse


    def getCircleRange(self):
        return self._circleRange


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 3:
            from watchFaceParser.models.elements.activity.pulseElement import PulseElement
            self._pulse = PulseElement(parameter = parameter, parent = self, name = '?Pulse?')
            return self._pulse
        elif parameterId == 5:
            from watchFaceParser.models.elements.activity.stepsElement import StepsElement
            self._steps = StepsElement(parameter = parameter, parent = self, name = '?Steps?')
            return self._steps
        elif parameterId == 9:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._circleRange = ImageElement(parameter = parameter, parent = self, name = '?Steps?')
            return self._circleRange
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

