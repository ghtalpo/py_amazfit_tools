import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AuxDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._month = None
        self._weekday = None
        super(AuxDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getMonth(self):
        return self._month


    def getWeekday(self):
        return self._weekday


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.auxDial.monthHandElement import MonthHandElement
            self._month = MonthHandElement(parameter = parameter, parent = self, name = 'Month')
            return self._month
        elif parameterId == 3:
            from watchFaceParser.models.elements.auxDial.weekdayHandElement import WeekdayHandElement
            self._weekday = WeekdayHandElement(parameter = parameter, parent = self, name = 'Weekday')
            return self._weekday
        else:
            return super(AuxDialElement, self).createChildForParameter(parameter)