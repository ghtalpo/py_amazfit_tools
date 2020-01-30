from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.dateElements.dateUnknown3 import DateUnknown3
from watchFaceParser.elements.dateElements.year import Year

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
        2: { 'Name': 'WeekDay', 'Type': ImageSet},
        3: { 'Name': 'Unknown3', 'Type': DateUnknown3},
        4: { 'Name': 'Unknown4', 'Type': Coordinates},
        5: { 'Name': 'Year', 'Type': Year},
    }

