import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement

class WeekDayProgressElement(IconSetElement):
    # private static readonly Dictionary<DayOfWeek, int> DaysOfWeek = new Dictionary<DayOfWeek, int>
    # {
    #     {DayOfWeek.Monday, 0},
    #     {DayOfWeek.Tuesday, 1},
    #     {DayOfWeek.Wednesday, 2},
    #     {DayOfWeek.Thursday, 3},
    #     {DayOfWeek.Friday, 4},
    #     {DayOfWeek.Saturday, 5},
    #     {DayOfWeek.Sunday, 6}
    # };

    def __init__(self, parameter, parent, name = None):
        self._ar = []
        #self._slices = 0
        super(WeekDayProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def getCoordinatesArray(self):
        return self._ar

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        # super(WeekDayElement, self).draw3(drawer, resources, DaysOfWeek[state.time.DayOfWeek]);
        #super(WeekDayProgressElement, self).draw3(drawer, resources, state.getTime().weekday())
        #print ("self.getCoordinates()",[c.getValue() for c in self.getCoordinates().getChildren()], self._slices, self._ar, len(self._ar))
        #print ("XXXX",len(self._ar))
        #for d in [c.getChildren() for c in self._ar]:
        #    print ("self.getCoordinates()",[c.getValue() for c in d])
        #if
        super(WeekDayProgressElement, self).draw3(drawer, resources, state.getTime().weekday(), cursor = True)

    def createChildForParameter(self, parameter):
        if parameter.getId() == 1:
            self._imageIndex = parameter.getValue()
            #print ("ARRAY",self._imageIndex)
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
            #print ( parameter.getValue(),parameter.getChildren())
        elif parameter.getId() == 2:
            #print ( [ c.getValue() for c in  parameter.getChildren()])
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            #print ( parameter.getValue(),parameter.getChildren())
            #print (self.getName(),[c.getValue() for c in parameter.getChildren()])
            #self._coordinates = [ CoordinatesElement(parameter = c, parent = self, name = 'CenterOffset') for c in parameter.getChildren()]
            #print (self._coordinates)
            self._coordinates = CoordinatesElement(parameter = parameter, parent = self, name = 'CenterOffset')
            self._ar.append(self._coordinates)
            #print (self._slices)
            #self._slices += 1
            #return self._coordinates
        else:
            super(IconSetElement, self).createChildForParameter(parameter)
