class Config:
    _is_gtr = False
    _image_size = 360


    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr:
            Config._image_size = 454


    @staticmethod
    def isGtrMode():
        return Config._is_gtr


    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return int(Config._image_size / 2)
