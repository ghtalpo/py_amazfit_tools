import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class CaloriesContainerElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        self._circularCalories = None
        self._clockHandCalories = None
        super(CaloriesContainerElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def getCircularCalories(self):
        return self._circularCalories

    def getClockHandCalories(self):
        return self._clockHandCalories

    def draw3(self, drawer, resources, state):

        if self.getCircularCalories():
            self.getCircularCalories().draw3(drawer, resources, state)

        if self.getClockHandCalories():
            self.getClockHandCalories().draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.activity.circularCaloriesElement import CircularCaloriesElement
            self._circularCalories = CircularCaloriesElement(parameter = parameter, parent = self, name = '_circularCalories')
        elif parameterId == 3:
            from watchFaceParser.models.elements.activity.caloriesClockHandElement import CaloriesClockHandElement
            self._clockHandCalories = CaloriesClockHandElement(parameter = parameter, parent = self, name = '_clockHandCalories')
        else:
            super(CaloriesContainerElement, self).createChildForParameter(parameter)
