from watchFaceParser.elements.timeElements.twoDigits import TwoDigits
from watchFaceParser.elements.unknown11Elements.unknownType11d1 import UnknownType11d1
from watchFaceParser.elements.unknown11Elements.unknownType11d2 import UnknownType11d2

class UnknownType11:
    definitions = {
        1: { 'Name': 'Unknown11_1', 'Type': [UnknownType11d1]},
        2: { 'Name': 'Unknown11_2', 'Type': UnknownType11d2},
    }
