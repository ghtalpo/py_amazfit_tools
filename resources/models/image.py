class Image:
    resourceExtension = '.png'

    @staticmethod
    def getExtension():
        return Image.resourceExtension


    def __init__(self, bitmap):
        self._bitmap = bitmap


    def getBitmap(self):
        return self._bitmap


    def writeTo(self, stream):
        from resources.image.writer import Writer
        Writer(stream).write(self._bitmap)


    def exportTo(self, stream):
        self._bitmap.save(stream)