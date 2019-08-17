import logging

class Color:
    @staticmethod
    def fromArgb(a, r = None, g = None, b = None):
        if r is None and g is None and b is None:
            v = a
            a = (v & 0xff000000) >> 24
            r = (v & 0xff0000) >> 16
            g = (v & 0xff00) >> 8
            b = (v & 0xff)
        return (r, g, b, a)

