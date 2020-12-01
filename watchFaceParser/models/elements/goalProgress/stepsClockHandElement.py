from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class StepsClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(StepsClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(StepsClockHandElement, self).draw4(drawer, resources,  state.getSteps(), state.getGoal())
