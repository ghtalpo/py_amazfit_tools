from watchFaceParser.models.elements.common.numberElement import NumberElement

class PulseElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(PulseElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getPulse():
            self.draw4(drawer, resources, state.getPulse())
