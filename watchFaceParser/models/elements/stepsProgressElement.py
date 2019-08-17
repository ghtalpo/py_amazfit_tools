import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class StepsProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        super(StepsProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getCircular(self):
        return self._circular


    # def getCircular2(self):
    #     return self._circular2


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 3:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
            self._circular = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular')
            return self._circular
        # elif parameterId == 5:
        #     from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
        #     self._circular2 = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular2')
        #     return self._circular2
        else:
            return super(StepsProgressElement, self).createChildForParameter(parameter)
