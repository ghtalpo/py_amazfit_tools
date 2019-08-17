import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement


class CircularBatteryElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(CircularBatteryElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CircularBatteryElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)

