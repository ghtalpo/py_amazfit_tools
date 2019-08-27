class Config:
    _is_gtr = False
    _image_size = 360
    _preview_size = 210


    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr:
            Config._image_size = 454
            Config._preview_size = 266


    @staticmethod
    def isGtrMode():
        return Config._is_gtr


    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return int(Config._image_size / 2)


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

