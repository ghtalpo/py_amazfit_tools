from watchFaceParser.models.elements.common.numberElement import NumberElement

class BatteryNumberElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(BatteryNumberElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        self.draw4(drawer, resources, state.getBatteryLevel())
