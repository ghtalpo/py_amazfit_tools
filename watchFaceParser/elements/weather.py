from watchFaceParser.elements.weatherElements.temperature import Temperature
from watchFaceParser.elements.weatherElements.icon import Icon
from watchFaceParser.elements.basicElements.number import Number

class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': Icon},
        2: { 'Name': 'Temperature', 'Type': Temperature},
    }
