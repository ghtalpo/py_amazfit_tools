from watchFaceParser.models.elements.common.switchElement import SwitchElement


class AlarmElement(SwitchElement):
    def __init__(self, parameter, parent, name = None):
        super(AlarmElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getAlarm()
