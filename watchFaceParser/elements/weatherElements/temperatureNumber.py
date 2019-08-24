from watchFaceParser.elements.basicElements.number import Number


class TemperatureNumber:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'MinusImageIndex', 'Type': 'long?'},
        3: { 'Name': 'DegreesImageIndex', 'Type': 'long?'},
    }

