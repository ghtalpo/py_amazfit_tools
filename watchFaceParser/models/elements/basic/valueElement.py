from watchFaceParser.models.elements.basic.element import Element

class ValueElement(Element):
    def __init__(self, parameter, parent, name):
        super(ValueElement, self).__init__(parameter, parent, name)
        self._value = parameter.getValue()

    def getValue(self):
        return self._value

