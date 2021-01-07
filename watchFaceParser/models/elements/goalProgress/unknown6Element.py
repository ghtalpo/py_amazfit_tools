from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class Unknown6Element(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(Unknown6Element, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        steps = state.getSteps()
        if state.getGoal() < steps:
            steps = state.getGoal()
        super(Unknown6Element, self).draw4(drawer, resources, steps, state.getGoal())
