from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class MonthHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(MonthHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(MonthHandElement, self).draw4(drawer, resources, state.getTime().month, 12)
