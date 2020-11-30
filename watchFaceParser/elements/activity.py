from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.distance import Distance
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.activityElements.caloriesContainer import CaloriesContainer
from watchFaceParser.elements.activityElements.pulseContainer import PulseContainer
from watchFaceParser.elements.basicElements.iconSet import IconSet

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
        12: { 'Name': 'ColouredSquares', 'Type': IconSet}, # gts - Classic number_101759
        13: { 'Name': 'UnknownImageIndex13', 'Type': 'long'},
        14: { 'Name': 'Unknown14', 'Type': 'long'}, # gts - Digital watch
        15: { 'Name': 'CaloriesTextualIcon', 'Type': 'long'}, # gts - Classic number_101759
        17: { 'Name': 'CaloriesGraph', 'Type': CaloriesContainer}, # gts circle.bin
        18: { 'Name': 'PulseGraph', 'Type': PulseContainer}, # gts fluorescence
    }

