import os
import logging

class Converter:
    width_gtr = 454
    width_verge_lite = 360
    width_bip = 176

    def __init__(self):
        self.source_size = 0
        self.target_size = Converter.width_verge_lite

    def loadJson(self, json_path):
        try:
            import json
            with open(json_path, 'rb') as stream:
                return json.load(stream)

        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    def saveJson(self, json_path, tree):
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


    def patchTree(self, tree, depth = 0):
        for k in tree:
            value = tree[k]
            if type(value) == int:
                if k.endswith('X') or k.endswith('Y') or k == 'Spacing':
                    tree[k] = int(value / self.source_size * self.target_size)
            elif type(value) == dict:
                self.patchTree(value, depth + 1)


    def resizeJson(self, json_path):
        tree = self.loadJson(json_path)

        # prevent PreviewStates.json from being parsed
        #  from (chenchix)
        if not 'Background' in tree:
            return

        self.patchTree(tree)
        self.saveJson(json_path, tree)


    def detectRatio(self, top_dir):
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
        raise Exception(f"Unsupported image source dimension({w}/{h})")


    def resizePng(self, top_dir):
        from PIL import Image
        self.detectRatio(top_dir)
        for root, _, files in os.walk(top_dir, topdown=False):
            for name in files:
                full_path = os.path.join(root, name)
                if name.endswith('.png'):
                    im = Image.open(full_path)
                    (w, h) = im.size
                    new_w = int(w * self.target_size / self.source_size)
                    new_h = int(h * self.target_size / self.source_size)
                    im = im.convert('RGBA')
                    im_resized = im.resize((new_w, new_h), resample = Image.LANCZOS)
                    im_resized.save(full_path)
                elif name.endswith('.json'):
                    self.resizeJson(full_path)
        print('Done...', top_dir)


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
        if not isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        Converter().resizePng(inputFileName)
