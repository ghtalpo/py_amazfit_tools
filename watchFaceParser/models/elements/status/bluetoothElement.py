from watchFaceParser.models.elements.common.switchElement import SwitchElement


class BluetoothElement(SwitchElement):
    def __init__(self, parameter, parent, name = None):
        super(BluetoothElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getBluetooth()
