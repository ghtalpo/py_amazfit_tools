import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class CircularGoalProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(CircularGoalProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CircularGoalProgressElement, self).draw4(drawer, resources, state.getSteps(), state.getGoal())
