from watchFaceParser.elements.weatherElements.separateTemperature import SeparateTemperature
from watchFaceParser.elements.weatherElements.onelineTemperature import OnelineTemperature


class TodayTemperature:
    definitions = {
        1: { 'Name': 'Separate', 'Type': SeparateTemperature},
        2: { 'Name': 'OneLine', 'Type': OnelineTemperature},
    }

