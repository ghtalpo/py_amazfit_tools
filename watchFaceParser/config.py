MODE_VL = 0
MODE_GTR = 1
MODE_GTS = 2
class Config:
    _mode = MODE_VL
    _dimensions = {
        MODE_VL: {
            "width": 360,
            "height": 360,
            "preview_width": 210,
            "preview_height": 210,
        },
        MODE_GTR: {
            "width": 454,
            "height": 454,
            "preview_width": 266,
            "preview_height": 266,
        },
        MODE_GTS: {
            "width": 348,
            "height": 442,
            "preview_width": 242,
            "preview_height": 304,
        },
    }


    @staticmethod
    def setGtrMode(gtr):
        if gtr == True:
            Config._mode = MODE_GTR


    @staticmethod
    def isGtrMode():
        return Config._mode == MODE_GTR


    @staticmethod
    def setGtsMode(gts):
        if gts == True:
            Config._mode = MODE_GTS


    @staticmethod
    def isGtsMode():
        return Config._mode == MODE_GTS


    @staticmethod
    def getDimensions():
        return Config._dimensions[Config._mode]


    @staticmethod
    def getImageWidth():
        return Config.getDimensions()["width"]


    @staticmethod
    def getImageWidthHalf():
        return int(Config.getImageWidth() / 2)


    @staticmethod
    def getImageHeight():
        return Config.getDimensions()["height"]


    @staticmethod
    def getImageHeightHalf():
        return int(Config.getImageHeight() / 2)


    @staticmethod
    def getPreviewWidth():
        return Config.getDimensions()["preview_width"]


    @staticmethod
    def getPreviewHeight():
        return Config.getDimensions()["preview_height"]

