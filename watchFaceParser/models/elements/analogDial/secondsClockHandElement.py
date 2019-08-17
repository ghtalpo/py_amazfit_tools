from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class SecondsClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(SecondsClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(SecondsClockHandElement, self).draw4(drawer, resources, state.getTime().second, 60)
