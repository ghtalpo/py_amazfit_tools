import datetime


class WatchState:
    def __init__(self, BatteryLevel = 67, Pulse = 62, Steps = 14876):
        self._time = datetime.datetime.now()
        self._steps = Steps
        self._goal = 8000
        self._pulse = Pulse
        self._batteryLevel = BatteryLevel


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


    def toJSON(self):
        return { 'Time': self.datetimeToJson(), 'Steps': self._steps, 'Goal': self._goal, 'Pulse': self._pulse, 'BatteryLevel': self._batteryLevel }


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
        return w

