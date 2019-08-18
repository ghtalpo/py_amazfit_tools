import os
import logging

original_size = 454 # gtr
target_size = 360 # verge lite


def loadJson(json_path):
    try:
        import json
        with open(json_path, 'rb') as stream:
            return json.load(stream)

    except Exception as e:
        logging.fatal(e, exc_info=True)
        return None


def saveJson(json_path, tree):
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


def patchTree(tree, depth = 0):
    for k in tree:
        value = tree[k]
        if type(value) == int:
            if k.endswith('X') or k.endswith('Y') or k == 'Spacing':
                tree[k] = int(value / original_size * target_size)
        elif type(value) == dict:
            patchTree(value, depth + 1)


def resizeJson(json_path):
    tree = loadJson(json_path)
    patchTree(tree)
    saveJson(json_path, tree)


def resizePng(top_dir):
    from PIL import Image, ImageDraw
    for root, _, files in os.walk(top_dir, topdown=False):
        for name in files:
            full_path = os.path.join(root, name)
            if name.endswith('.png'):
                im = Image.open(full_path)
                (w, h) = im.size
                new_w = int(w * target_size / original_size)
                new_h = int(h * target_size / original_size)
                im_resized = im.resize((new_w, new_h), resample = Image.LANCZOS)
                im_resized.save(full_path)
            elif name.endswith('.json'):
                resizeJson(full_path)
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
        resizePng(inputFileName)
