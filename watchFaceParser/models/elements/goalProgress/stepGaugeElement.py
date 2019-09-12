import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class StepGaugeElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(StepGaugeElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(StepGaugeElement, self).draw3(drawer, resources, int(state.getSteps() / state.getGoal() * self.getImagesCount()))

