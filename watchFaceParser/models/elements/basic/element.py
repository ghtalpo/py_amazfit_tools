import logging


class Element:
    def __init__(self, parameter, parent, name = None):
        self._id = parameter.getId()
        self._name = name
        self._parent = parent


    def hasParent(self):
        return self._parent != None


    def getStringId(self):
        return str(self._id)


    def getId(self):
        return self._id


    def getName(self):
        return self._name if self._name is not None else f"Unknown{self._id}"


    def getPath(self):
        if self.hasParent():
            return f"{self._parent.getPath()}.{self.getStringId()}"
        else:
            return self.getStringId()

