class FileDescriptor:
    def __init__(self, Resources = []):
        # self.hasNewHeader = False
        # self.resourcesCount = 0
        # self.unknown = 0
        # self.version = 0
        self.resources = Resources

    # def HasNewHeader(self):
    #     return self.hasNewHeader

    # def ResourcesCount(self):
    #     return self.resourcesCount

    # def Unknown(self):
    #     return self.unknown

    # def Version(self):
    #     return self.version

    def getResources(self):
        return self.resources
