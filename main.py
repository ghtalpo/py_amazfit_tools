import os
import logging


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage example:")
        print(" %s watchface.bin - unpacks watchface images and config" % (sys.argv[0]))
        print(" %s watchface.json - packs config and referenced images to bin file" % (sys.argv[0]))
        sys.exit(1)
    args = sys.argv[1:]
    if len(args) > 1:
        print("Multitple files unpacking")
    for inputFileName in args:
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exists." % (inputFileName, ))
            continue
        if isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            import program
            if inputFileExtension == '.bin':
                program.Parser.unpackWatchFace(inputFileName)
            elif inputFileExtension == '.json':
                program.Parser.packWatchFace(inputFileName)
            else:
                print("The app doesn't support file with extension %s." % (inputFileExtension, ))
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e, ))
            import traceback
            traceback.print_stack()
            logging.exception(e)

