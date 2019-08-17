from watchFaceParser.elements.basicElements.number import Number

class SeparateMonthAndDay:
    definitions = {
        1: { 'Name': 'Month', 'Type': Number},
        3: { 'Name': 'Day', 'Type': Number},
    }
