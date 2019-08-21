import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class StatusElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._bluetooth = None
        self._unlocked = None
        self._alarm = None
        self._doNotDisturb = None
        super(StatusElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getBluetooth(self):
        return self._bluetooth


    def getUnlocked(self):
        return self._unlocked


    def getAlarm(self):
        return self._alarm


    def getDoNotDisturb(self):
        return self._doNotDisturb


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 4:
            from watchFaceParser.models.elements.status.bluetoothElement import BluetoothElement
            self._bluetooth = BluetoothElement(parameter = parameter, parent = self, name = 'Bluetooth')
            return self._bluetooth
        elif parameterId == 3:
            from watchFaceParser.models.elements.status.unlockedElement import UnlockedElement
            self._unlocked = UnlockedElement(parameter = parameter, parent = self, name = 'Unlocked')
            return self._unlocked
        elif parameterId == 2:
            from watchFaceParser.models.elements.status.alarmElement import AlarmElement
            self._alarm = AlarmElement(parameter = parameter, parent = self, name = 'Alarm')
            return self._alarm
        elif parameterId == 1:
            from watchFaceParser.models.elements.status.doNotDisturbElement import DoNotDisturbElement
            self._doNotDisturb = DoNotDisturbElement(parameter = parameter, parent = self, name = 'DoNotDisturb')
            return self._doNotDisturb
        else:
            return super(StatusElement, self).createChildForParameter(parameter)
