# py amazfit tool
An python port of valeronm's amazfitbiptools(v.1.0.3.1) with some hacks for verge lite/gtr.

All credit goes to Валерий Миронов(https://bitbucket.org/valeronm/amazfitbiptools/src/master/)

## what is...
* can pack/unpack .bin file for amazfit verge lite/gtr(original watchfaces)

## what isn't...
* 100% compatibility with amazfit_bip_tool
* 100% compatibility with .json structures of bip

## requirements
* python3(tested on 3.7.4)
* pillow(tested on 6.1.0)

## usage
* for verge lite
  * see scripts folder
    * to unpack
      * python main.py WATCH_FACE_FILE.bin
    * to pack
      * python main.py WATCH_FACE_FILE.json
    * to convert from extracted GTR watchface(experimental BIP support also)
      * python convert.py EXTRACTED_WATCH_FACE_FOLDER
  * for windows users(experimental) : USE AT YOUR OWN RISK
    * copy & unzip amazfit_verge_lite_tools_WIN32.zip from release/win32
      * to pack
        * drag & drop WATCH_FACE_FILE.json into main/main.exe
      * to unpack
        * drag & drop WATCH_FACE_FILE.bin into main/main.exe
      * to convert from extracted GTR watchface(experimental BIP support also)
        * drag & drop EXTRACTED_WATCH_FACE_FOLDER into convert/convert.exe
* for GTR(47mm)
  * to unpack
    * python main.py --gtr WATCH_FACE_FILE.bin
  * to pack
    * python main.py --gtr WATCH_FACE_FILE.json
  * for windows users(experimental) : USE AT YOUR OWN RISK
    * copy & unzip amazfit_gtr_tools_WIN32.7z from release/win32
      * to pack
        * drag & drop WATCH_FACE_FILE.json into main_gtr/main.exe
      * to unpack
        * drag & drop WATCH_FACE_FILE.bin into main_gtr/main.exe

## known issues in json
### Date/Weekday/ImageCount (GTR(47mm))
* Unlike verge lite, Date/Weekday/ImagesCount should be 21 instead of 7

```
  "Date": {
    "WeekDay": {
      "X": 242,
      "Y": 122,
      "ImageIndex": 128,
      "ImagesCount": 21
    }
  },
```
### status icons
#### lock & bluetooth icons broken (Verge Lite)
#### working for (GTR(47mm))
* use GTR branch

### analog hands' relative position (only works for GTR(47mm))

## why python instead of C#
just for fun!
