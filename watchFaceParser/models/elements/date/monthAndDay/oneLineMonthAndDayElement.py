import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.integerConverter import uint2int


class OneLineMonthAndDayElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._delimiterImageIndex = None
        super(OneLineMonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getNumber(self):
        return self._number


    def getDelimiterImageIndex(self):
        return self._delimiterImageIndex.getValue()


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        monthAndDay = self._parent

        images = self.getNumber().getImagesForNumber(resources, state.getTime().month, 2 if monthAndDay.getTwoDigitsMonth() else 1)

        images.append(resources[self.getDelimiterImageIndex()])
        for image in self.getNumber().getImagesForNumber(resources, state.getTime().day, 2 if monthAndDay.getTwoDigitsDay() else 1):
            images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self.getNumber().getSpacing()), self.getNumber().getAlignment(), self.getNumber().getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = ValueElement(parameter = parameter, parent = self, name = 'WeekDay')
            return self._delimiterImageIndex
        else:
            return super(OneLineMonthAndDayElement, self).createChildForParameter(parameter)
