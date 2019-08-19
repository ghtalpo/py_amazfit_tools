from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.distance import Distance
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image

class Activity:
    definitions = {
        1: { 'Name': 'Steps1', 'Type': Number},
        2: { 'Name': 'StepsGoal', 'Type': Number},
        3: { 'Name': 'Pulse', 'Type': Number},
        4: { 'Name': 'Distance', 'Type': Distance},
        5: { 'Name': 'Steps', 'Type': FormattedNumber},
        7: { 'Name': 'StarImage', 'Type': Image}, #gtr
        9: { 'Name': 'CircleRange', 'Type': Image}, # verge
    }

