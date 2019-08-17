import os.path
import logging


class extractor:
    def __init__(self, descriptor):
        self._descriptor = descriptor


    def extract(self, outputDirectory):
        from resources.imageLoader import ImageLoader
        for i in range(len(self._descriptor.getResources())):
            resource = self._descriptor.getResources()[i]
            numericPart = str(i).zfill(ImageLoader.NumericPartLength)

            fileName = os.path.join(outputDirectory, numericPart + resource.getExtension())
            logging.debug(f"extracting {fileName}...")

            with open(fileName, 'wb') as fileStream:
                resource.exportTo(fileStream)