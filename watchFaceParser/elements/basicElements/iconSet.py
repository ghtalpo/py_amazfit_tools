from watchFaceParser.elements.basicElements.coordinates import Coordinates

class IconSet:
    definitions = {
        1: { 'Name': 'ImageIndex', 'Type': 'long'},
        2: { 'Name': 'Coordinates', 'Type': [Coordinates]},
    }

