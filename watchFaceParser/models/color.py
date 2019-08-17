import logging

class Color:
    def __init__(self, v):
        self.r = (v & 0xff000000) >> 24
        self.g = (v & 0xff0000) >> 16
        self.b = (v & 0xff00) >> 8
        self.a = (v & 0xff)


    def toJSON(self):
        return f"0x{self.r:02X}{self.g:02X}{self.b:02X}{self.a:02X}"


    @staticmethod
    def fromJSON(strValue):
        v = int(strValue, 16)
        return v

