from watchFaceParser.elements.basicElements.number import Number


class OnelineTemperature:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'MinusSignImageIndex', 'Type': 'long'},
        3: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        4: { 'Name': 'AppendDegreesForBoth', 'Type': 'bool'},
        5: { 'Name': 'DegreesImageIndex', 'Type': 'long'},
    }

