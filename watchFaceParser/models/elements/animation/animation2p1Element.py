import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class Animation2p1Element(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        self._parent = parent
        super(Animation2p1Element, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        delay = self._parent.getAnimation2p2() # TODO: is it a delay?
        MAGIC_CONST = 16.6667
        super(Animation2p1Element, self).draw3(drawer, resources, int(state.getAnimationSeq() * delay / MAGIC_CONST) % self.getImagesCount())
