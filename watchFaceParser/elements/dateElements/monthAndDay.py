from watchFaceParser.elements.dateElements.separateMonthAndDay import SeparateMonthAndDay
from watchFaceParser.elements.dateElements.oneLineMonthAndDay import OneLineMonthAndDay

class MonthAndDay:
    definitions = {
        1: { 'Name': 'Separate', 'Type': SeparateMonthAndDay},
        2: { 'Name': 'OneLine', 'Type': OneLineMonthAndDay},
        3: { 'Name': 'TwoDigitsMonth', 'Type': 'bool'},
        4: { 'Name': 'TwoDigitsDay', 'Type': 'bool'},
    }
