from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.weatherElements.customWeatherIcon import CustomWeatherIcon


class WeatherIcon:
    definitions = {
        1: { 'Name': 'Coordinates', 'Type': Coordinates},
        2: { 'Name': 'CustomIcon', 'Type': CustomWeatherIcon},
        3: { 'Name': 'CoordinatesAlt', 'Type': Coordinates},
        4: { 'Name': 'Unknown4', 'Type': Coordinates},
    }

#     // For compatibility with "Unknown3" JSON attribute
#     [JsonProperty("Unknown3")]
#     private Coordinates Unknown3
#     {
#         set { CoordinatesAlt = value; }
#     }
# }