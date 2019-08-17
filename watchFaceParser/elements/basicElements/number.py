from watchFaceParser.models.textAlignment import TextAlignment

class Number:
    definitions = {
        1: { 'Name': 'TopLeftX', 'Type': 'long'},
        2: { 'Name': 'TopLeftY', 'Type': 'long'},
        3: { 'Name': 'BottomRightX', 'Type': 'long'},
        4: { 'Name': 'BottomRightY', 'Type': 'long'},
        5: { 'Name': 'Alignment', 'Type': TextAlignment},
        6: { 'Name': 'Spacing', 'Type': 'long'},
        7: { 'Name': 'ImageIndex', 'Type': 'long'},
        8: { 'Name': 'ImagesCount', 'Type': 'long'},
    }