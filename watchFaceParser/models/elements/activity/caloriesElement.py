from watchFaceParser.models.elements.common.numberElement import NumberElement

class CaloriesElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(CaloriesElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        super(CaloriesElement, self).draw4(drawer, resources, state.getCalories())
