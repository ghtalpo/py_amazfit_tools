from watchFaceParser.elements.statusElements.switch import Switch

class Status:
    definitions = {
        4: { 'Name': 'DoNotDisturb', 'Type': Switch},
        1: { 'Name': 'Bluetooth', 'Type': Switch},
        2: { 'Name': 'Alarm', 'Type': Switch},
        3: { 'Name': 'Lock', 'Type': Switch},
    }

