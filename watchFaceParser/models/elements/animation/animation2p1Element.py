import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class Animation2p1Element(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(Animation2p1Element, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(Animation2p1Element, self).draw3(drawer, resources, state.getAnimationSeq() % self.getImagesCount())
