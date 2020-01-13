from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.distance import Distance
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.circleScale import CircleScale

class Activity:
    definitions = {
        1: { 'Name': 'CaloriesCircle', 'Type': CircleScale}, #gtr only?
        2: { 'Name': 'Calories', 'Type': Number},
        3: { 'Name': 'Pulse', 'Type': Number},
        4: { 'Name': 'Distance', 'Type': Distance},
        5: { 'Name': 'Steps', 'Type': FormattedNumber},
        7: { 'Name': 'StarImage', 'Type': Image},
        9: { 'Name': 'CircleRange', 'Type': Image},
        11: { 'Name': 'PulseCircle', 'Type': CircleScale},
        13: { 'Name': 'UnknownImageIndex13', 'Type': 'long'},
    }

