import os.path
import logging


class ImageLoader:
    NumericPartLength = 4

    @staticmethod
    def loadResourceForNumber(directory, index):
        assert(type(directory) == str)
        assert(type(index) == int)

        strIndex = str(index)
        numericParts = sorted(set([strIndex.zfill(4), strIndex.zfill(3), strIndex.zfill(2), strIndex]), key=len, reverse=True)

        for numericPart in numericParts:
            resource = ImageLoader.tryLoadBitmap(directory, numericPart)
            if resource != None:
                return resource

        raise FileNotFoundException(f"File referenced by index {index} not found.")


    @staticmethod
    def tryLoadBitmap(directory, numericPart):
        assert(type(directory) == str)
        assert(type(numericPart) == str)

        from resources.models.image import Image

        fullFileName = os.path.join(directory, numericPart + Image.resourceExtension)
        if not os.path.exists(fullFileName):
            logging.debug(f"File {fullFileName} doesn't exist.")
            return None

        image = ImageLoader.openImage(fullFileName)
        return Image(image)

    @staticmethod
    def openImage(fullFileName):
        from PIL import Image
        image = Image.open(fullFileName)
        return image
