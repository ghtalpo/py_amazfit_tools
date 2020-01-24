from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.unknown6 import Unknown6

class ClockHand:
    definitions = {
        1: { 'Name': 'unknown1', 'Type': 'long'},
        2: { 'Name': 'unknown2', 'Type': 'long'},
        3: { 'Name': 'CenterOffset', 'Type': Coordinates},
        4: { 'Name': 'unknown4', 'Type': Coordinates},
        5: { 'Name': 'Image', 'Type': Image},
        6: { 'Name': 'unknown6', 'Type': Unknown6},
    }

