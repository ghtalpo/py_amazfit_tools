import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement


class CircularCaloriesElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(CircularCaloriesElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CircularCaloriesElement, self).draw4(drawer, resources, state.getCalories(), 800)
