class ParameterFlags:
    Default = 0
    Unknown = 1
    hasChildren = 2
    Unknown2 = 4

    ModeCircle = Unknown
    ModeColorfulLife = Unknown | hasChildren | Unknown2
    ModeFluorescence = hasChildren

    Converter = {
        Default : "Default",
        ModeColorfulLife : "ModeColorfulLife",
        ModeCircle : "ModeCircle",
		ModeFluorescence: "ModeFluorescence",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def getValue(self):
        return self._flag

    def toJSON(self):
        return ParameterFlags.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ParameterFlags.Converter:
            if strFlag == ParameterFlags.Converter[flag]:
                return flag
        return 0