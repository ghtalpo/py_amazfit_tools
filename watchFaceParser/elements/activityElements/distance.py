from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.models.color import Color

class Distance:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long?'},
        3: { 'Name': 'DecimalPointImageIndex', 'Type': 'long?'},
        4: { 'Name': 'Color', 'Type': Color},
    }

