from watchFaceParser.elements.statusElements.switch import Switch

class Status:
    definitions = {
        1: { 'Name': 'Bluetooth', 'Type': Switch},
        2: { 'Name': 'Alarm', 'Type': Switch},
        3: { 'Name': 'Lock', 'Type': Switch},
        4: { 'Name': 'DoNotDisturb', 'Type': Switch},
    }

