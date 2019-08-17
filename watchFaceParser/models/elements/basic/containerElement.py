from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
import logging

class ContainerElement(CompositeElement):
    def __init__(self, parameters, parameter, parent, name):
        super(ContainerElement, self).__init__(parameters, parameter, parent, name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        for element in self.getDrawableChildren():
            element.draw3(drawer, images, state)
