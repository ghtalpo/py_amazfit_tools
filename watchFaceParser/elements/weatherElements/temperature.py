from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.weatherElements.today import Today
from watchFaceParser.elements.weatherElements.symbols import Symbols

class Temperature:
    definitions = {
        1: { 'Name': 'Current', 'Type': Number},
        2: { 'Name': 'Today', 'Type': Today},
        3: { 'Name': 'Symbols', 'Type': Symbols},
    }

