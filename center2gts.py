import os
import logging

class Converter:
    width_gtr = 454
    width_gtr_42 = 390
    width_verge_lite = 360
    width_bip = 176
    width_gts = 348
    height_gts = 442

    def __init__(self):
        self.source_size = 0
        self.target_width = Converter.width_gts
        self.target_height = Converter.height_gts

    def _loadJson(self, json_path):
        try:
            import json
            with open(json_path, 'rb') as stream:
                return json.load(stream)

        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    def _saveJson(self, json_path, tree):
        try:
            import json
            def dumper(obj):
                try:
                    return obj.toJSON()
                except AttributeError:
                    return obj.__dict__

            with open(json_path, 'w') as stream:
                stream.write(json.dumps(tree, default=dumper, indent = 2))
                stream.flush()
        except Exception as e:
            logging.fatal(e, exc_info=True)


    def _patchTree(self, tree, depth = 0):
        for k in tree:
            if k == 'AnalogDialFace' or k == 'ClockHand' or k == 'Unknown4' or k == 'DaysProgress': # skip these sections
                continue
            value = tree[k]
            if type(value) == int:
                if not k.startswith('Radius'):
                    if k.endswith('X'):
                        tree[k] = int(value - (self.source_size - self.target_width)/2)
                    if k.endswith('Y'):
                        tree[k] = int(value - (self.source_size - self.target_height)/2)
            elif type(value) == dict:
                self._patchTree(value, depth + 1)
            elif type(value) == list:
                self._patchList(value, depth + 1)


    def _patchList(self, list, depth = 0):
        for v in list:
            if type(v) == dict:
                self._patchTree(v, depth + 1)


    def convertJson(self, json_path):
        tree = self._loadJson(json_path)

        # prevent PreviewStates.json from being parsed
        #  from (chenchix)
        if not 'Background' in tree:
            return

        self._patchTree(tree)
        self._saveJson(json_path, tree)


    def _detectSource(self, top_dir):
        target_path = os.path.join(top_dir, '0000.png')
        from PIL import Image
        im = Image.open(target_path)
        (w, h) = im.size
        if w == h:
            if w == Converter.width_gtr:
                self.source_size = Converter.width_gtr
                print('GTR source')
                return
            elif w == Converter.width_bip:
                self.source_size = Converter.width_bip
                print('BIP source')
                return
            elif w == Converter.width_gtr_42:
                self.source_size = Converter.width_gtr_42
                print('GTR(42) source')
                return
            elif w == Converter.width_verge_lite:
                self.source_size = Converter.width_verge_lite
                print('VL source')
                return
        raise Exception(f"Unsupported image source dimension({w}/{h})")


    def execute(self, top_dir):
        from PIL import Image
        self._detectSource(top_dir)
        for root, _, files in os.walk(top_dir, topdown=False):
            for name in files:
                full_path = os.path.join(root, name)
                if name.endswith('.json'):
                    self.convertJson(full_path)
        print('Done...', top_dir)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage example:")
        print(" %s path - make centered .json for GTS " % (sys.argv[0]))
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
        if not isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        Converter().execute(inputFileName)
