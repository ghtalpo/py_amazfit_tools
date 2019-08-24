from watchFaceParser.elements.weatherElements.temperatureNumber import TemperatureNumber
from watchFaceParser.elements.weatherElements.todayTemperature import TodayTemperature


class Temperature:
    definitions = {
        1: { 'Name': 'Current', 'Type': TemperatureNumber},
        2: { 'Name': 'Today', 'Type': TodayTemperature},
    }

