import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TimeElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        # self._drawingOrder = None
        self._delimiter = None
        super(TimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getHours(self):
        return self._hours


    def getMinutes(self):
        return self._minutes


    def getSeconds(self):
        return self._seconds


    def getAmPm(self):
        return self._amPm


    # def getDrawingOrder(self):
    #     return self._drawingOrder


    def getDelimeter(self):
        return self._delimiter

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        if self.getAmPm():
            self.getAmPm().draw3(drawer, images, state)

        hours = state.getTime().hour if self.getAmPm() is None else state.getTime().hour % 12
        # drawingOrder = 0x1234 if self.getDrawingOrder() is None else self.getDrawingOrder()

        if self.getHours() and self.getHours().getTens():
            self.getHours().getTens().draw3(drawer, images, int(hours % 100 / 10))
        if self.getHours() and self.getHours().getOnes():
            self.getHours().getOnes().draw3(drawer, images, hours % 10)
        if self.getMinutes() and self.getMinutes().getTens():
            self.getMinutes().getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
        if self.getMinutes() and self.getMinutes().getOnes():
            self.getMinutes().getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self.getSeconds():
            self.getSeconds().draw3(drawer, images, state.getTime().second)
        if self.getDelimeter():
            self.getDelimeter().draw3(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._hours = TwoDigitsElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._minutes = TwoDigitsElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._seconds = TwoDigitsElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        elif parameterId == 4:
            from watchFaceParser.models.elements.time.amPmElement import AmPmElement
            self._amPm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
            return self._amPm
        elif parameterId == 5:
            pass
        elif parameterId == 10:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._delimiter = ImageElement(parameter = parameter, parent = self, name = 'Delimiter')
            return self._delimiter
        else:
            return super(TimeElement, self).createChildForParameter(parameter)

