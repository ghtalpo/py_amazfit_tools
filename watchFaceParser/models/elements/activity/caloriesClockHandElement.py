from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

#fixme... implement angle and more in CLockhandElement
class CaloriesClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(CaloriesClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CaloriesClockHandElement, self).draw4(drawer, resources, state.getCalories(), 700)
