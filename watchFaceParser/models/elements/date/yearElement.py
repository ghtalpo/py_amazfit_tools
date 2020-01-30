import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class YearElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._separate = None
        super(YearElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getSeparate(self):
        return self._separate


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.date.year.separateYearElement import SeparateYearElement
            self._separate = SeparateYearElement(parameter = parameter, parent = self, name = 'SeparateYearElement')
            return self._separate
        else:
            return super(YearElement, self).createChildForParameter(parameter)

