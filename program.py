import os.path
import logging
import json


from watchFaceParser.reader import Reader
from watchFaceParser.writer import Writer
from watchFaceParser.utils.parametersConverter import ParametersConverter
from watchFaceParser.utils.resourcesLoader import ResourcesLoader
from watchFaceParser.watchFace import WatchFace
from watchFaceParser.models.fileDescriptor import FileDescriptor
from watchFaceParser.models.watchState import WatchState
from watchFaceParser.previewGenerator import PreviewGenerator


def dumper(obj):
    try:
        return obj.toJSON()
    except AttributeError:
        return obj.__dict__


class Parser:
    @staticmethod
    def createOutputDirectory(originalFileName):
        path = os.path.dirname(originalFileName)
        name, _ = os.path.splitext(os.path.basename(originalFileName))
        unpackedPath = os.path.join(path, name)
        if not os.path.exists(unpackedPath):
            os.mkdir(unpackedPath)
        return unpackedPath


    @staticmethod
    def readWatchFaceConfig(jsonFileName):
        assert(type(jsonFileName) == str)
        logging.debug("Reading config...")
        try:
            with open(jsonFileName, 'rb') as fileStream:
                return json.load(fileStream)

        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    @staticmethod
    def setupLogger(logFileName):
        logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


    @staticmethod
    def writeWatchFace(outputDirectory, outputFileName, imagesDirectory, watchFace):
        assert(type(outputDirectory) == str)
        assert(type(outputFileName) == str)
        assert(type(imagesDirectory) == str)
        try:
            logging.debug(f"Reading referenced images from '{imagesDirectory}'")
            imagesReader = ResourcesLoader(imagesDirectory)
            imagesReader.process(WatchFace, watchFace)

            logging.debug("Building parameters for watch face...")
            descriptor = ParametersConverter.build(WatchFace, watchFace)

            baseName, _ = os.path.splitext(os.path.basename(outputFileName))
            Parser.generatePreviews(descriptor, imagesReader.getImages(), outputDirectory, baseName)

            logging.debug(f"Writing watch face to '{outputFileName}'")
            with open(outputFileName, 'wb') as fileStream:
                writer = Writer(fileStream, imagesReader.resources())
                writer.write(descriptor)
                fileStream.flush()
        except Exception as e:
            logging.fatal(e, exc_info=True)
            os.remove(outputFileName)


    @staticmethod
    def readWatchFace(inputFileName):
        logging.debug(f"Opening watch face '{inputFileName}'")
        try:
            with open(inputFileName, 'rb') as fileStream:
                reader = Reader(fileStream)
                logging.debug("Reading parameters...")
                reader.read()
                return reader
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
            return None


    @staticmethod
    def packWatchFace(inputFileName):
        assert(type(inputFileName) == str)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        outputDirectory = os.path.dirname(inputFileName)
        outputFileName = os.path.join(outputDirectory, f"{baseName}_packed.bin")
        Parser.setupLogger(os.path.join(outputDirectory, f'{baseName}_packed.log'))

        watchFace = Parser.readWatchFaceConfig(inputFileName)

        t = json.dumps(watchFace, default=dumper, indent = 2)
        logging.debug(f't: {t}')
        if not watchFace:
            return

        imagesDirectory = os.path.dirname(inputFileName)
        try:
            Parser.writeWatchFace(outputDirectory, outputFileName, imagesDirectory, watchFace)
        except Exception as e:
            os.remove(outputFileName)
            raise e


    @staticmethod
    def unpackWatchFace(inputFileName):
        outputDirectory = Parser.createOutputDirectory(inputFileName)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        Parser.setupLogger(os.path.join(outputDirectory, f'{baseName}.log'))

        reader = Parser.readWatchFace(inputFileName)
        if not reader:
            return

        watchFace = Parser.parseResources(reader)
        if not watchFace:
            return

        logging.debug("generatePreviews")
        Parser.generatePreviews(reader.getParameters(), reader.getImages(), outputDirectory, baseName)
        logging.debug("generatePreviews done")

        logging.debug("Exporting resources to '%s'" % (outputDirectory, ))
        reDescriptor = FileDescriptor(Resources = reader.getResources())

        from resources.extractor import extractor
        extractor(reDescriptor).extract(outputDirectory)
        Parser.exportWatchFaceConfig(watchFace, os.path.join(outputDirectory, f'{baseName}.json'))


    @staticmethod
    def exportWatchFaceConfig(watchFace, jsonFileName):
        assert(type(jsonFileName) == str)
        logging.debug("Exporting config...")
        try:
            with open(jsonFileName, 'w') as fileStream:
                fileStream.write(json.dumps(watchFace, default=dumper, indent = 2))
                fileStream.flush()
        except Exception as e:
            logging.fatal(e, exc_info=True)


    @staticmethod
    def parseResources(reader):
        logging.debug("Parsing parameters...")
        try:
            return ParametersConverter.parse(WatchFace, reader.getParameters())
        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    @staticmethod
    def generatePreviews(parameters, images, outputDirectory, baseName):
        assert(type(parameters) == list)
        assert(type(images) == list)
        assert(type(outputDirectory) == str)
        assert(type(baseName) == str)

        logging.debug("Generating previews...")

        states = Parser.getPreviewStates(outputDirectory)
        logging.debug("Generating states done...")
        staticPreview = PreviewGenerator.createImage(parameters, images, WatchState())
        logging.debug("Generating static preview gen done...")
        staticPreview.save(os.path.join(outputDirectory, f"{baseName}_static.png"))

        # generate small preview image for Preview section.
        from PIL import Image
        new_w, new_h = 210, 210
        im_resized = staticPreview.resize((new_w, new_h), resample = Image.LANCZOS)
        im_resized.save(os.path.join(outputDirectory, f"{baseName}_static_210.png"))
        logging.debug("Generating static preview save done...")

        previewImages = PreviewGenerator.createAnimation(parameters, images, states)
        logging.debug("Generating anim preview gen done...")

        images = []
        for previewImage in previewImages:
            images.append(previewImage)
        images[0].save(os.path.join(outputDirectory, f"{baseName}_animated.gif"),
            save_all=True,
            append_images=images[1:],
            duration=1000,
            loop=0)


    @staticmethod
    def getPreviewStates(outputDirectory):
        import os
        previewStatesPath = os.path.join(outputDirectory, "PreviewStates.json")

        if os.path.exists(previewStatesPath):
            try:
                with open(previewStatesPath, 'rb') as stream:
                    return WatchState.fromJson(json.load(stream))
            except:
                pass

        previewStates = Parser.generateSampleStates()
        with open(previewStatesPath, 'w') as stream:
            stream.write(json.dumps(previewStates, default=dumper, indent = 2))
            stream.flush()

        return previewStates


    @staticmethod
    def generateSampleStates():
        import datetime
        time = datetime.datetime.now()
        states = []

        for i in range(10):
            num = i + 1
            watchState = WatchState(
                BatteryLevel = 100 - i * 10,
                Pulse = 60 + num * 2,
                Steps = num * 1000,
                Calories = num * 75,
                Distance = num * 700,
                Bluetooth = num > 1 and num < 6,
                Unlocked = num > 2 and num < 7,
                Alarm = num > 3 and num < 8,
                DoNotDisturb = num > 4 and num < 9,
            )

            watchState.setTime(datetime.datetime(year = time.year, month = num, day = num * 2 + 5, hour = i * 2, minute = i * 6, second = i))
            states.append(watchState)

        return states
