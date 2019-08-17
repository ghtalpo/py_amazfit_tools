import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class WeekDayElement(ImageSetElement):
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
        super(WeekDayElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        # super(WeekDayElement, self).draw3(drawer, resources, DaysOfWeek[state.time.DayOfWeek]);
        super(WeekDayElement, self).draw3(drawer, resources, state.getTime().weekday())
