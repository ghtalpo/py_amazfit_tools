from watchFaceParser.models.elements.common.imageElement import ImageElement


class StarImageElement(ImageElement):
    def __init__(self, parameter, parent, name = None):
        super(StarImageElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getGoal() <= state.getSteps():
            super(StarImageElement, self).draw3(drawer, resources, state)
