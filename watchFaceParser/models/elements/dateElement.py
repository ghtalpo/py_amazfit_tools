import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._monthAndDay = None
        self._weekDay = None
        self._year = None
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getMonthAndDay(self):
        return self._monthAndDay


    def getWeekDay(self):
        return self._weekDay


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.date.monthAndDayElement import MonthAndDayElement
            self._monthAndDay = MonthAndDayElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._monthAndDay
        elif parameterId == 2:
            from watchFaceParser.models.elements.date.weekDayElement import WeekDayElement
            self._weekDay = WeekDayElement(parameter = parameter, parent = self, name = 'WeekDay')
            return self._weekDay
        elif parameterId == 5:
            from watchFaceParser.models.elements.date.yearElement import YearElement
            self._year = YearElement(parameter = parameter, parent = self, name = 'Year')
            return self._year
        else:
            return super(DateElement, self).createChildForParameter(parameter)
