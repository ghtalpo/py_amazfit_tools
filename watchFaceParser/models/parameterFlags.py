class ParameterFlags:
    Unknown = 1
    hasChildren = 2
    Unknown2 = 4

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

