from watchFaceParser.elements.weatherElements.temperatureNumber import TemperatureNumber
from watchFaceParser.elements.basicElements.coordinates import Coordinates


class SeparateTemperature:
    definitions = {
        1: { 'Name': 'Day', 'Type': TemperatureNumber},
        2: { 'Name': 'Night', 'Type': TemperatureNumber},
        3: { 'Name': 'DayAlt', 'Type': Coordinates},
        4: { 'Name': 'NightAlt', 'Type': Coordinates},
    }

        # // For compatibility with "Unknown3" JSON attribute
        # [JsonProperty("Unknown3")]
        # private Coordinates Unknown3
        # {
        #     set { DayAlt = value; }
        # }

        # // For compatibility with "Unknown4" JSON attribute
        # [JsonProperty("Unknown4")]
        # private Coordinates Unknown4
        # {
        #     set { NightAlt = value; }
        # }

