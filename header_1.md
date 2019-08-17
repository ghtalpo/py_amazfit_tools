# headers
## 1 (analog)
### name
* 1b5d5d8-48-73b52218e4

### file size
* 810160 (0xc5e72)

### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6eea 0000 01bc ffff ffff ffff ffff   .n.............
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5100 0000 1f00 0000 4000 0000  ....Q.......@...
> [00000000,00000040) : header parameterSize(0x1f(31))
> 00000040: 0a05 08a1 0110 2112 0408 0010 1022 0408  ......!......"..
> 00000050: 3910 172a 0408 1010 2952 0408 5010 51
> * Reader.read
>  * "Reading parameters descriptor..."
>  * Parameter.readFrom(paramStream)
>    rawId(0x0a) -> _id(1), flags(2)
>    val(0x05) 5
>    * Parameter.readList([0x08, 0xa1, 0x01, 0x10, 0x21])
>     * Parameter.readFrom([0x08, 0xa1, 0x01, 0x10, 0x21])
>       rawId(0x08) -> _id(1), flag(0)
>       val(0xa1) 161 ======================> parametersTableLength
>       rawId(0x10) -> _id(2), flag(0)
>       val(0x21) 33 ========================> imagesCount
>  * "Reading parameters locations..."
>  * Parameter.readList([0x12, 0x04, 0x08, 0x00, 0x10, 0x10, 0x22, 0x04, 0x08, 0x39, 0x10, 0x17, 0x2a, 0x04, 0x08, 0x10, 0x10, 0x29, x052, x04, x08, 0x50, 0x10, 0x51])
>   * Parameter.readFrom(0x12, 0x04, 0x08, 0x00, 0x10, 0x10, 0x22, 0x04, 0x08, 0x39, 0x10, 0x17, 0x2a, 0x04, 0x08, 0x10, 0x10, 0x29, x052, x04, x08, 0x50, 0x10, 0x51])

> 00000050:                                      0a  9..*....)R..P.Q.
> 00000060: 0608 0010 0018 001a 0608 0010 0018 010a  ................
> 00000070: 1d12 170a 1308 b501 1060 18e6 0120 8701  .........`... ..
> 00000080: 2812 3001 3802 400a 100c 1801 2001 1208  (.0.8.@..... ...
> 00000090: 087f 1060 180d 2007 2a15 0a13 0800 10f3  ...`.. .*.......
> 000000a0: 0118 e802 2098 0228 1830 0138 1440 0a0a  .... ..(.0.8.@..
> 000000b0: 1908 0010 001a 0408 0010 0022 0408 0010  ..........."....
> 000000c0: 002a 0708 1510 8901 181e 1219 0800 1000  .*..............
> 000000d0: 1a04 0800 1000 2204 0800 1000 2a07 0813  ......".....*...
> 000000e0: 109a 0118 1f1a 1908 0010 001a 0408 0010  ................
> 000000f0: 0022 0408 0010 002a 0708 0c10 a901 1820  .".....*.......

> 00000100: 0000 0000 18e9 0700 409a 0a00 889c 0a00  ........@.......
> 00000110: d09e 0a00 18a1 0a00 60a3 0a00 a8a5 0a00  ........`.......
> 00000120: f0a7 0a00 38aa 0a00 80ac 0a00 c8ae 0a00  ....8...........
> 00000130: 10b1 0a00 78b2 0a00 80bd 0a00 88c8 0a00  ....x...........
> 00000140: 90d3 0a00 98de 0a00 a0e9 0a00 a8f4 0a00  ................
> 00000150: b0ff 0a00 f802 0b00 4006 0b00 8809 0b00  ........@.......
> 00000160: d00c 0b00 1810 0b00 6013 0b00 a816 0b00  ........`.......
> 00000170: f019 0b00 381d 0b00 8020 0b00 cc90 0b00  ....8.... ......
> 00000180: a001 0c00

## 2 (digital)
### name
* 57fe98717b51fa82778f4f3d2b016581-33826-794be8368a

### file size
* 997804 (0xf39ac)

### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6dea 0000 8177 ffff ffff ffff ffff   .m....w........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 4700 0000

## 3 (digital)
### name
* da76d2189933bc8a6bc2af75e4ea72f0-33826-81f82f40f1.bin

### file size
* 914,756 (0xdf544)

### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6aea 0000 b1f3 ffff ffff ffff ffff   .j.............
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 3c00 0000 1800 0000 4000 0000  ....<.......@...
> [00000000,00000040) : header parameterSize(0x18(24))

> * Reader.read
>  * "Reading parameters descriptor..."
>  * Parameter.readFrom(paramStream)
>    rawId(0x0a) -> _id(1), flags(2)
>    val(0x04) 4
>    * Parameter.readList([0x08, 0x77, 0x10, 0x1f])
>     * Parameter.readFrom([0x08, 0x77, 0x10, 0x1f])
>       rawId(0x08) -> _id(1), flag(0)
>       val(0x77) 119 ======================> parametersTableLength
>       rawId(0x10) -> _id(2), flag(0)
>       val(0x1f) 31 ========================> imagesCount
>  * "Reading parameters locations..."
>     12 04 08 10 10 10 2: 1/ 0 2/ 16
>     1a 04 08 10 10 3c 3: 1/ 16 2/ 60
>     2a 04 08 4c 10 2b 4: 1/ 76 2/ 43
> 00000040: 0a04 0877 101f 1204 0800 1010 1a04 0810  ...w............
> 00000050: 103c 2a04 084c 102b

> * for BackgroundElement(2)
> 00000050:                     0a06 0800 1000 1800  .<*..L.+........
> 00000060: 1a06 0800 1000 1801

> * for TimeElement(3)
> 00000060:                     0a16 0a09 083c 10e7  .............<..
> 00000070: 0118 0220 0a12 0908 7210 e701 1802 200a  ... ....r..... .
> 00000080: 1218 0a0a 08c5 0110 e701 1802 200a 120a  ............ ...
> 00000090: 08ff 0110 e701 1802 200a 5208 08af 0110  ........ .R.....
> 000000a0: e701 180c

> - 1 ( A): 22 bytes        : 0a16
> -     1 ( A): 9 bytes     : 0a09
> -         1 ( 8): 60 3C   : 083c
> -         2 (10): 231 E7  : 10e7 01
> -         3 (18): 2  2    : 18 02
> -         4 (20): 10  A   : 20 0a
> -     2 (12): 9 bytes     : 12 09
> -         1 ( 8): 114 72  : 08 72
> -         2 (10): 231 E7  : 10 e701
> -         3 (18): 2  2    : 1802
> -         4 (20): 10  A   : 200a
> - 2 (12): 24 bytes        : 1218
> -     1 ( A): 10 bytes    : 0a0a
> -         1 ( 8): 197 C5  : 08c5 01
> -         2 (10): 231 E7  : 10 e701
> -         3 (18): 2  2    : 1802
> -         4 (20): 10  A   : 200a
> -     2 (12): 10 bytes    : 120a
>                           : 08ff 01
>                           : 10 e701
>                           : 18 02
>                           : 20 0a
> - 10 (52): 8 bytes        : 5208
> -     1 ( 8): 175 AF      : 08af 01
> -     2 (10): 231 E7      : 10 e7
> -     3 (18): 12  C       : 01 180c

> 000000a0:           0a1e 1218 0a14 08b3 0110 b802  ................
> 000000b0: 1898 0220 de02 2812 3002 380d 400a 1017  ... ..(.0.8.@...
> 000000c0: 1801 2001 1209 0869 10b7 0218 1820 0701  .. ....i..... ..
> 000000d0: 0000 0019 e907 0041 9a0a 00c9 d90a 0051  .......A.......Q
> 000000e0: 190b 00d9 580b 0061 980b 00e9 d70b 0071  ....X..a.......q
> 000000f0: 170c 00f9 560c 0081 960c 0009 d60c 0091  ....V...........
> 00000100: 150d 0079 360d 0011 3b0d 00a9 3f0d 0041  ...y6...;...?..A
> 00000110: 440d 00d9 480d 0071 4d0d 0009 520d 00a1  D...H..qM...R...
> 00000120: 560d 0039 5b0d 00d1 5f0d 0069 640d 0051  V..9[..._..id..Q
> 00000130: 670d 0069 7b0d 0081 8f0d 0099 a30d 00b1  g..i{...........
> 00000140: b70d 00c9 cb0d 00e1 df0d 00ff

## 4 (analog)
### name
* de7b1104-48-ea9f70b645.bin
### file size
* 791,876 ()
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 69ea 0000 74fa ffff ffff ffff ffff   .i...t.........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5000 0000

## 5 (analog)
### name
* 2eac844-48-4e4254dc71.bin
### file size
* 707,960 ()
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6bea 0000 7c3e ffff ffff ffff ffff   .k...|>........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5a00 0000 1200 0000 4000 0000  ....Z.......@...
> [00000000,00000040) : header parameterSize(0x12(18))
> 00000040: 0a04 0874 1007 1204 0800 101a 5204 081a  ...t........R...
> 00000050: 105a
> * Reader.read
>  * "Reading parameters descriptor..."
>  * Parameter.readFrom(paramStream)
>    rawId(0x0a) -> _id(1), flags(2)
>    val(0x04) 4
>    * Parameter.readList([0x08, 0x74, 0x10, 0x07])
>     * Parameter.readFrom([0x08, 0x74, 0x10, 0x07])
>       rawId(0x08) -> _id(1), flag(0)
>       val(0x74) 116 ======================> parametersTableLength?
>       rawId(0x10) -> _id(2), flag(0)
>       val(0x07) 7 ========================> imagesCount?
>  * "Reading parameters locations..."
>  * Parameter.readList([0x12, 0x04, 0x08, 0x00, 0x10, 0x1a, 0x52, 0x04, 0x08, 0x1a, 0x10, 0x5a])
>   * Parameter.readFrom([0x12, 0x04, 0x08, 0x00, 0x10, 0x1a, 0x52, 0x04, 0x08, 0x1a, 0x10, 0x5a])
>       rawId(0x12) -> _id(3), flag(2)
>       val(0x04) 04
>      * Parameter.readList([0x08, 0x00, 0x10, 0x1a])
>       rawId(0x08) -> _id(1), flag(0)
>       val(0x10) 16
>       rawId(0x10) -> _id(2), flag(0)
>       val(0x1a) 26
>   * Parameter.readFrom([0x52, 0x04, 0x08, 0x1a, 0x10, 0x5a])
>       rawId(0x52) -> _id(10), flag(2)
>       val(0x04) 04
>      * Parameter.readList([0x08, 0x1a, 0x10, 0x5a])
>       * Parameter.readFrom([0x08, 0x1a, 0x10, 0x5a])
>        rawId(0x08) -> _id(1), flag(0)
>        val(0x1a) 26
>        rawId(0x10) -> _id(2), flag(0)
>        val(0x5a) 90
>  * Reader.readParameters(116, ...)
> 00000050:      0a06 0800 1000 1800 1a06 0800 1000  .Z..............
> 00000060: 1801 2208 08a7 0110 a801 1802 0a18 0800  ..".............
> 00000070: 1000 1a04 0800 1000 2204 0800 1000 2a06  ........".....*.
> 00000080: 0803 1076 1803 1219 0800 1000 1a04 0800  ...v............
> 00000090: 1000 2204 0800 1000 2a07 0802 1098 0118  ..".....*.......
> 000000a0: 041a 1908 0010 001a 0408 0010 0022 0408  ............."..
> 000000b0: 0010 002a 0708 0110 9c01 1805 2208 08af  ...*........"...
> 000000c0: 0110 af01 1806
>
>  * resources.reader.Reader().read(7)
> 000000c0:                0200 0000 5ef4 0700 86a5  ..........^.....
> 000000d0: 0a00 2eb0 0a00 9ebb 0a00 56c5 0a00 eeca  ..........V.....
> 000000e0: 0a00 ffff

## 6 (digital)
### name
* d126a9f-48-2a91eb35b2.bin
### file size
* 876,164 ()
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6fea 0000 14de ffff ffff ffff ffff   .o.............
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 3a00 0000

## 7 (digital)
### name
* ebaa6-48-2bde1a96c8.bin
### file size
* 849,124 ()
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 70ea 0000 35a1 ffff ffff ffff ffff   .p...5.........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 3600 0000

## 8 (analog)
### name
* 6d11de6-48-50a39f979f.bin
### file size
* 1,262,096 ()
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6cea 0000 3f2c ffff ffff ffff ffff   .l...?,........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5000 0000

## 9 (digital)
### name
* test_packed_01-07-43-46288-6da8a09e2f
### file size
* 914,756
### header
> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6aea 0000 b1f3 ffff ffff ffff ffff   .j.............
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 3c00 0000