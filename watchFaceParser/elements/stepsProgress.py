from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand

class StepsProgress:
    definitions = {
        1: { 'Name': 'Images1', 'Type': ImageSet}, # test
        2: { 'Name': 'Images2', 'Type': ImageSet}, # test
        4: { 'Name': 'Images4', 'Type': ImageSet}, # test
        3: { 'Name': 'Circle', 'Type': CircleScale},
        5: { 'Name': 'Unknown5', 'Type': CircleScale}, # verge
        6: { 'Name': 'Unknown6', 'Type': ClockHand}, #?
    }
