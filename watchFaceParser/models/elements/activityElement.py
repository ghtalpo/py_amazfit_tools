import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._stepsGoal = None
        self._steps = None
        self._distance = None
        self._pulse = None
        self._calories = None
        self._starImage = None
        self._circleRange = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getStepsGoal(self):
        return self._stepsGoal


    def getSteps(self):
        return self._steps


    def getDistance(self):
        return self._distance


    def getPulse(self):
        return self._pulse


    def getCalories(self):
        return self._calories


    def getStarImage(self):
        return self._starImage


    def getCircleRange(self):
        return self._circleRange


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.activity.stepsGoalElement import StepsGoalElement
            self._stepsGoal = StepsGoalElement(parameter = parameter, parent = self, name = '?StepsGoal?')
            return self._stepsGoal
        elif parameterId == 2:
            from watchFaceParser.models.elements.activity.caloriesElement import CaloriesElement
            self._calories = CaloriesElement(parameter = parameter, parent = self, name = '?Calories?')
            return self._calories
        elif parameterId == 3:
            from watchFaceParser.models.elements.activity.pulseElement import PulseElement
            self._pulse = PulseElement(parameter = parameter, parent = self, name = '?Pulse?')
            return self._pulse
        elif parameterId == 4:
            from watchFaceParser.models.elements.activity.distanceElement import DistanceElement
            self._distance = DistanceElement(parameter = parameter, parent = self, name = '?DistanceElement?')
            return self._distance
        elif parameterId == 5:
            from watchFaceParser.models.elements.activity.stepsElement import StepsElement
            self._steps = StepsElement(parameter = parameter, parent = self, name = '?Steps?')
            return self._steps
        elif parameterId == 7:
            from watchFaceParser.models.elements.activity.starImageElement import StarImageElement
            self._starImage = StarImageElement(parameter = parameter, parent = self, name = '?StarImage?')
            return self._starImage
        elif parameterId == 9:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._circleRange = ImageElement(parameter = parameter, parent = self, name = '?CircleRange?')
            return self._circleRange
        elif parameterId == 12:
            from watchFaceParser.models.elements.activity.pulseLinearElement import PulseLinearElement
            self._pulseLinear = PulseLinearElement(parameter = parameter, parent = self, name = '?pulseLinear?')
            return self._pulseLinear
        elif parameterId == 11:
            from watchFaceParser.models.elements.activity.pulseMeterElement import PulseMeterElement
            self._pulseMeter = PulseMeterElement(parameter = parameter, parent = self, name = '?PulseMeter?')
            return self._pulseMeter
        elif parameterId == 17:
            from watchFaceParser.models.elements.activity.caloriesContainerElement import CaloriesContainerElement
            self._caloriesContainer = CaloriesContainerElement(parameter = parameter, parent = self, name = '?CaloriesContainer?')
            return self._caloriesContainer
        elif parameterId == 18:
            from watchFaceParser.models.elements.activity.pulseContainerElement import PulseContainerElement
            self._pulseContainer = PulseContainerElement(parameter = parameter, parent = self, name = '?PulseContainer?')
            return self._pulseContainer
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

