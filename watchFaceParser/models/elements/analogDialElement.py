import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        super(AnalogDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getHours(self):
        return self._hours


    def getMinutes(self):
        return self._minutes


    def getSeconds(self):
        return self._seconds


    def getCenterImage(self):
        return self._centerImage


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.elements.analogDial.secondsClockHandElement import SecondsClockHandElement
            self._seconds = SecondsClockHandElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._centerImage = ImageElement(parameter = parameter, parent = self, name = 'CenterImage')
            return self._centerImage
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)