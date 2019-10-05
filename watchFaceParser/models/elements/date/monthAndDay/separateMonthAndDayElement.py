import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SeparateMonthAndDayElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._month = None
        self._monthName = None
        self._day = None
        super(SeparateMonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getMonth(self):
        return self._month

    
    def getMonthName(self):
        return self._monthName

    
    def getDay(self):
        return self._day


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        monthAndDay = self._parent

        if self.getMonth():
            self.getMonth().draw4(drawer, resources, state.getTime().month, 2 if monthAndDay.getTwoDigitsMonth() else 1)
        if self.getMonthName():
            self.getMonthName().draw3(drawer, resources, state.getTime().month-1)
        if self.getDay():
            self.getDay().draw4(drawer, resources, state.getTime().day, 2 if monthAndDay.getTwoDigitsDay() else 1)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter = parameter, parent = self, name = 'Month')
            return self._month
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._monthName = ImageSetElement(parameter = parameter, parent = self, name = 'MonthName')
            return self._monthName
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter = parameter, parent = self, name = 'Day')
            return self._day
        else:
            return super(SeparateMonthAndDayElement, self).createChildForParameter(parameter)
