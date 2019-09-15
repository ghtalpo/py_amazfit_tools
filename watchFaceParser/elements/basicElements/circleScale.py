from watchFaceParser.models.color import Color

class CircleScale:
    definitions = {
        1: { 'Name': 'CenterX', 'Type': 'long'},
        2: { 'Name': 'CenterY', 'Type': 'long'},
        3: { 'Name': 'RadiusX', 'Type': 'long'},
        4: { 'Name': 'RadiusY', 'Type': 'long'},
        5: { 'Name': 'StartAngle', 'Type': 'long'},
        6: { 'Name': 'EndAngle', 'Type': 'long'},
        7: { 'Name': 'Width', 'Type': 'long'},
        8: { 'Name': 'Color', 'Type': Color},
        9: { 'Name': 'Flatness', 'Type': 'long'}, #verge
    }
