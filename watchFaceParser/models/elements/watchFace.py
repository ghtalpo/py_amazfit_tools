from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
        self._time = None
        self._activity = None
        self._date = None
        self._weather = None
        self._stepsProgress = None
        self._status = None
        self._battery = None
        self._analogDial = None
        self._auxDial = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')


    def getBackground(self):
        return self._background


    def getTime(self):
        return self._time


    def getActivity(self):
        return self._activity


    def getDate(self):
        return self._date


    def getWeather(self):
        return self._weather


    def getStepsProgress(self):
        return self._stepsProgress


    def getStatus(self):
        return self._status


    def getBattery(self):
        return self._battery


    def getAnalogDial(self):
        return self._analogDial


    def getAuxDial(self):
        return self._auxDial


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 2:
            from watchFaceParser.models.elements.backgroundElement import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 3:
            from watchFaceParser.models.elements.timeElement import TimeElement
            self._time = TimeElement(parameter)
            return self._time
        elif parameterId == 4:
            from watchFaceParser.models.elements.activityElement import ActivityElement
            self._activity = ActivityElement(parameter)
            return self._activity
        elif parameterId == 5:
            from watchFaceParser.models.elements.dateElement import DateElement
            self._date = DateElement(parameter)
            return self._date
        elif parameterId == 6:
            from watchFaceParser.models.elements.weatherElement import WeatherElement
            self._weather = WeatherElement(parameter)
            return self._weather
        elif parameterId == 7:
            from watchFaceParser.models.elements.stepsProgressElement import StepsProgressElement
            self._stepsProgress = StepsProgressElement(parameter)
            return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            from watchFaceParser.models.elements.batteryElement import BatteryElement
            self._battery = BatteryElement(parameter)
            return self._battery
        elif parameterId == 10:
            from watchFaceParser.models.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial
        elif parameterId == 15:
            from watchFaceParser.models.elements.auxDialElement import AuxDialElement
            self._auxDial = AuxDialElement(parameter)
            return self._auxDial
        else:
            return super(WatchFace, self).createChildForParameter(parameter)
