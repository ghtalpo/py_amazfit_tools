from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class Unknown4Element(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(Unknown4Element, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(Unknown4Element, self).draw4(drawer, resources, state.getBatteryLevel(), 100)
