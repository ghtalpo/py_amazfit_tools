from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class PulseMeterElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(PulseMeterElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getPulse():
            self.draw4(drawer, resources, state.getPulse(), 150)