import datetime

from watchFaceParser.models.weatherCondition import WeatherCondition


class WatchState:
    def __init__(self, BatteryLevel = 67, Pulse = 62, Steps = 14876, Calories = 764, Distance = 2367, Bluetooth = False, Unlocked = False, Alarm = False, DoNotDisturb = False, DayTemperature = -15, NightTemperature = -24):
        self._time = datetime.datetime.now().replace(hour = 10, minute = 10, second = 30)
        self._steps = Steps
        self._goal = 8000
        self._distance = Distance
        self._calories = Calories
        self._pulse = Pulse
        self._batteryLevel = BatteryLevel
        self._bluetooth = Bluetooth
        self._unlocked = Unlocked
        self._alarm = Alarm
        self._doNotDisturb = DoNotDisturb
        self._currentWeather = WeatherCondition.PartlyCloudy
        self._currentTemperature = -10
        self._dayTemperature = DayTemperature
        self._nightTemperature = NightTemperature


    def getTime(self):
        return self._time


    def setTime(self, _time):
        self._time = _time


    def getSteps(self):
        return self._steps


    def getGoal(self):
        return self._goal


    def getPulse(self):
        return self._pulse


    def getBatteryLevel(self):
        return self._batteryLevel


    def getDistance(self):
        return self._distance


    def getCalories(self):
        return self._calories


    def getBluetooth(self):
        return self._bluetooth


    def getUnlocked(self):
        return self._unlocked


    def getAlarm(self):
        return self._alarm


    def getDoNotDisturb(self):
        return self._doNotDisturb


    def getCurrentWeather(self):
        return self._currentWeather


    def setCurrentWeather(self, weather):
        assert(type(weather) == int)
        self._currentWeather = weather


    def getCurrentTemperature(self):
        return self._currentTemperature


    def setCurrentTemperature(self, temperature):
        assert(type(temperature) == int or temperature is None)
        self._currentTemperature = temperature


    def getDayTemperature(self):
        return self._dayTemperature


    def getNightTemperature(self):
        return self._nightTemperature


    def toJSON(self):
        return {
            'Time': self.datetimeToJson(),
            'Steps': self._steps,
            'Goal': self._goal,
            'Pulse': self._pulse,
            'BatteryLevel': self._batteryLevel,
            'Distance': self._distance,
            'Calories': self._calories,
            'Bluetooth': self._bluetooth,
            'Unlocked': self._unlocked,
            'Alarm': self._alarm,
            'DoNotDisturb': self._doNotDisturb,
            'CurrentWeather': self._currentWeather,
            'CurrentTemperature': self._currentTemperature,
            'DayTemperature': self._dayTemperature,
            'NightTemperature': self._nightTemperature,
        }

    def datetimeToJson(self):
        t = self._time
        return { 'Year': t.year, 'Month': t.month, 'Day': t.day, 'Hour': t.hour, 'Minute': t.minute, 'Second': t.second }


    @staticmethod
    def fromJson(j):
        w = WatchState()
        w._time = j['Time']
        w._steps = j['Steps']
        w._goal = j['Goal']
        w._pulse = j['Pulse']
        w._batteryLevel = j['BatteryLevel']
        w._distance = j['Distance']
        w._calories = j['Calories']
        w._bluetooth = j['Bluetooth']
        w._unlocked = j['Unlocked']
        w._alarm = j['Alarm']
        w._doNotDisturb = j['DoNotDisturb']
        w._currentWeather = j['CurrentWeather']
        w._currentTemperature = j['CurrentTemperature']
        w._dayTemperature = j['DayTemperature']
        w._nightTemperature = j['NightTemperature']
        return w

