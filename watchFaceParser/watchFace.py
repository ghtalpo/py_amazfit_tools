from watchFaceParser.elements.background import Background
from watchFaceParser.elements.time import Time
from watchFaceParser.elements.activity import Activity
from watchFaceParser.elements.date import Date
from watchFaceParser.elements.stepsProgress import StepsProgress
from watchFaceParser.elements.status import Status
from watchFaceParser.elements.battery import Battery
from watchFaceParser.elements.analogDialFace import AnalogDialFace
from watchFaceParser.elements.unknownType11 import UnknownType11
from watchFaceParser.elements.unknownType14 import UnknownType14
from watchFaceParser.elements.weather import Weather
from watchFaceParser.elements.auxDialFace import AuxDialFace
from watchFaceParser.elements.shortcuts import Shortcuts

class WatchFace:
    definitions = {
        2: { 'Name': 'Background', 'Type': Background},
        3: { 'Name': 'Time', 'Type': Time},
        4: { 'Name': 'Activity', 'Type': Activity},
        5: { 'Name': 'Date', 'Type': Date},
        6: { 'Name': 'Weather', 'Type': Weather},
        7: { 'Name': 'StepsProgress', 'Type': StepsProgress},
        8: { 'Name': 'Status', 'Type': Status},
        9: { 'Name': 'Battery', 'Type': Battery},
        10: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace},
        11: { 'Name': 'Unknown11', 'Type': UnknownType11},
        14: { 'Name': 'Unknown14', 'Type': UnknownType14},
        15: { 'Name': 'AuxDialFace', 'Type': AuxDialFace},
        16: { 'Name': 'Shortcuts', 'Type': Shortcuts},
    }
