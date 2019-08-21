from watchFaceParser.models.elements.common.switchElement import SwitchElement


class DoNotDisturbElement(SwitchElement):
    def __init__(self, parameter, parent, name = None):
        super(DoNotDisturbElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getDoNotDisturb()
