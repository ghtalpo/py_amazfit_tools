import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class MonthAndDayElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._oneLine = None
        self._separate = None
        self._twoDigitsMonth = None
        self._twoDigitsDay = None
        super(MonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getOneLine(self):
        return self._oneLine


    def getSeparate(self):
        return self._separate


    def getTwoDigitsMonth(self):
        return self._twoDigitsMonth


    def getTwoDigitsDay(self):
        return self._twoDigitsDay


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.date.monthAndDay.separateMonthAndDayElement import SeparateMonthAndDayElement
            self._separate = SeparateMonthAndDayElement(parameter = parameter, parent = self, name = 'SeparateMonthAndDayElement')
            return self._separate
        elif parameterId == 2:
            from watchFaceParser.models.elements.date.monthAndDay.oneLineMonthAndDayElement import OneLineMonthAndDayElement
            self._oneLine = OneLineMonthAndDayElement(parameter = parameter, parent = self, name = 'OneLineMonthAndDayElement')
            return self._oneLine
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._twoDigitsMonth = parameter.getValue() == 1
            return ValueElement(parameter = parameter, parent = self, name = 'TwoDigitsMonth')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._twoDigitsDay = parameter.getValue() == 1
            return ValueElement(parameter = parameter, parent = self, name = 'TwoDigitsDay')
        else:
            return super(MonthAndDayElement, self).createChildForParameter(parameter)

