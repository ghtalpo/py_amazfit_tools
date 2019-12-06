from watchFaceParser.elements.basicElements.imageSet import ImageSet

class WeatherIcon:
    definitions = {
        1: { 'Name': 'CustomIcon', 'Type': ImageSet},
        3: { 'Name': 'ExIcon', 'Type': 'long?'},
    }