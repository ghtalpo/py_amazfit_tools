# amazfit verge lite tool
An python port of valeronm's amazfitbiptools(v.1.0.3.1) with some hack for verge lite.

All credit goes to Валерий Миронов(https://bitbucket.org/valeronm/amazfitbiptools/src/master/)

## what is...
* can pack/unpack .bin file for amazfit verge lite(original watchfaces)

## what isn't...
* 100% conversion from amazfit_bip_tool
* 100% compatibility with .json structures of bip

## requirements
* python3(tested on 3.7.4)
* pillow(tested on 6.1.0)

## usage
* see scripts folder
  * to unpack
python main.py WATCH_FACE_FILE.bin
  * to pack
python main.py WATCH_FACE_FILE.json
  * to convert from extracted GTR watchface
python convert.py EXTRACTED_WATCH_FACE_FOLDER

## why python instead of C#
just for fun!
