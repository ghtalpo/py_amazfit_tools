import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class BatteryGaugeElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryGaugeElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryGaugeElement, self).draw3(drawer, resources, int(state.getBatteryLevel() * self.getImagesCount() / 100))
