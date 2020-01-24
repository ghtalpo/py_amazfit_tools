from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class WeekdayHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(WeekdayHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(WeekdayHandElement, self).draw4(drawer, resources, state.getTime().weekday(), 7)
