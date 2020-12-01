import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class PulseContainerElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        self._pulseClockHand = None
        super(PulseContainerElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def getPulseClockHand(self):
        return self._pulseClockHand

    def draw3(self, drawer, resources, state):

        if self.getPulseClockHand():
            self.getPulseClockHand().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 2:
            from watchFaceParser.models.elements.activity.pulseClockHandElement import PulseClockHandElement
            self._pulseClockHand = PulseClockHandElement(parameter = parameter, parent = self, name = '?ClockHand?')
            return self._pulseClockHand
        else:
            super(PulseContainerElement, self).createChildForParameter(parameter)
