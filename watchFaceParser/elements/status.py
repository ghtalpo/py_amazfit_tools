from watchFaceParser.elements.statusElements.switch import Switch

class Status:
    definitions = {
        1: { 'Name': 'DoNotDisturb', 'Type': Switch},
        2: { 'Name': 'Lock', 'Type': Switch},
        3: { 'Name': 'Alarm', 'Type': Switch},
        4: { 'Name': 'Bluetooth', 'Type': Switch},
    }

