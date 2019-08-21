from watchFaceParser.elements.basicElements.coordinates import Coordinates

class Switch:
    definitions = {
        1: { 'Name': 'Coordinates', 'Type': Coordinates},
        2: { 'Name': 'ImageIndexOn', 'Type': 'long?'},
        3: { 'Name': 'ImageIndexOff', 'Type': 'long?'},
    }

