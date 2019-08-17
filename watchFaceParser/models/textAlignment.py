class TextAlignment:
    Left = 2
    Right = 4
    HCenter = 8

    Top = 16
    Bottom = 32
    VCenter = 64

    TopCenter = Top | HCenter
    TopLeft = Top | Left
    TopRight = Top | Right

    Center = VCenter | HCenter
    CenterLeft = VCenter | Left
    CenterRight = VCenter | Right

    BottomCenter = Bottom | HCenter
    BottomLeft = Bottom | Left
    BottomRight = Bottom | Right

    Converter = {
        TopCenter : "TopCenter",
        TopLeft : "TopLeft",
        TopRight : "TopRight",
        Center : "Center",
        CenterLeft : "CenterLeft",
        CenterRight : "CenterRight",
        BottomCenter : "BottomCenter",
        BottomLeft : "BottomLeft",
        BottomRight : "BottomRight",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        return TextAlignment.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in TextAlignment.Converter:
            if strFlag == TextAlignment.Converter[flag]:
                return flag
        return 0
