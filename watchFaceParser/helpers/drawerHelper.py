class DrawerHelper:
    @staticmethod
    def calculateBounds(images, spacing):
        assert(type(images) == list)
        assert(type(spacing) == int)

        width = 0
        height = 0

        for image in images:
            imageWidth = image.getBitmap().size[0]
            imageHeight = image.getBitmap().size[1]

            width += imageWidth + spacing
            if imageHeight > height:
                height = imageHeight

        width -= spacing
        return (int(width), height)


    @staticmethod
    def drawImages(drawer, images, spacing, alignment, box):
        assert(type(images) == list)
        assert(type(spacing) == int)
        assert(type(alignment) == int)

        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)

        from watchFaceParser.models.textAlignment import TextAlignment
        alignmentFlag = TextAlignment(alignment)

        x = 0
        y = 0
        if alignmentFlag.hasFlag(TextAlignment.Left):
            x = box.getX()
        elif alignmentFlag.hasFlag(TextAlignment.Right):
            x = box.getRight() - bitmapWidth + 1
        else:
            x = (box.getLeft() + box.getRight() - bitmapWidth) >> 1

        if alignmentFlag.hasFlag(TextAlignment.Top):
            y = box.getTop()
        elif alignmentFlag.hasFlag(TextAlignment.Bottom):
            y = box.getBottom() - bitmapHeight + 1
        else:
            y = (box.getTop() + box.getBottom() - bitmapHeight) >> 1

        if x < box.getLeft():
            x = box.getLeft()
        if y < box.getTop():
            y = box.getTop()

        for image in images:
            temp = image.getBitmap()
            drawer.paste(temp, (x,y), temp)

            imageWidth = image.getBitmap().size[0]
            x += imageWidth + int(spacing)
