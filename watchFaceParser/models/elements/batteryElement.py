import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config
from watchFaceParser.utils.integerConverter import uint2int


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._percent = None
        self._scale = None
        self._images = None
        self._unknown4 = None
        self._batteryLinear = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getText(self):
        return self._text


    def getPercent(self):
        return self._percent


    def getScale(self):
        return self._scale


    def getImages(self):
        return self._images


    def getBatteryLinear(self):
        return self._batteryLinear


    def getUnknown4(self):
        return self._unknown4


    # override for percent of GTS
    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        shouldPatchPercent = False
        if self.getText() and self.getPercent() and self.getPercent().getX() == 0 and self.getPercent().getY() == 0:
            # is this hack needed for GTR also?
            shouldPatchPercent = True

        if shouldPatchPercent:
            resources = images
            assert(type(resources) == list)
            battery = state.getBatteryLevel()

            imagesTmp = self.getText().getImagesForNumber(resources, battery)
            imagesTmp.append(resources[self.getPercent().getImageIndex()])

            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, imagesTmp, uint2int(self.getText().getSpacing()), self.getText().getAlignment(), self.getText().getBox())
        else:
            if self.getText():
                self.getText().draw3(drawer, images, state)

            if self.getPercent():
                self.getPercent().draw3(drawer, images, state)

        if self.getScale():
            self.getScale().draw3(drawer, images, state)

        if self.getImages():
            self.getImages().draw3(drawer, images, state)

        if self.getBatteryLinear():
            self.getBatteryLinear().draw3(drawer, images, state)

        if self.getUnknown4():
            self.getUnknown4().draw3(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            from watchFaceParser.models.elements.battery.batteryNumberElement import BatteryNumberElement
            self._text = BatteryNumberElement(parameter = parameter, parent = self, name = '?_text?')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.elements.battery.batteryGaugeElement import BatteryGaugeElement # temp.
            self._images = BatteryGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images
        elif parameterId == 6:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._percent = ImageElement(parameter = parameter, parent = self, name = '?_percent?')
            return self._percent
        elif parameterId == 7:
            from watchFaceParser.models.elements.battery.circularBatteryElement import CircularBatteryElement
            self._scale = CircularBatteryElement(parameter = parameter, parent = self, name = '_scale')
            return self._scale
        elif parameterId == 3: #icons - this is the circular battery element found in GTS - Silver Watchface
            from watchFaceParser.models.elements.battery.batteryLinearElement import BatteryLinearElement
            self._batteryLinear = BatteryLinearElement(parameter = parameter, parent = self, name = '?pulseLinear?')
            return self._batteryLinear
        elif parameterId == 4: #unknown4
            from watchFaceParser.models.elements.battery.unknown4Element import Unknown4Element
            self._unknown4 = Unknown4Element(parameter = parameter, parent = self, name = 'Unknown4')
            return self._unknown4
        else:
            return super(BatteryElement, self).createChildForParameter(parameter)

