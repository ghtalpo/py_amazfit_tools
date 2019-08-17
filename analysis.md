# analysis

## bip
### simple_packed.bin

#### header
> 00000000: 484d 4449 414c 00ff ffff ffff ffff ffff  HMDIAL..........
> 00000010: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000020: 5901 0000 1800 0000 0a04 0828 1012 1204  Y..........(....
>                               id:1,flag:2,len:4
>                                    0828 1012
>                                    id:1,value:0x28
>                                    id:2,value:0x12
>                              (1)[parameter descriptor] parameterTableLength:40, imageCount:18
>                                              id:2,flag:2,len:4
>                                           (2)[Watch face parameters locations]
> 00000030: 0800 1008 1a04 0808 1016 2a04 081e 100a  ..........*.....
>           0800 1008
>           id:1,value:0
>           id:2,value:8
>           [2:[{1,0},{2,8}]]
>                     id:3,flag:2,len:4
>                         0808 1016
>                         id:1,value:8
>                         id:2,value:16
>                        +[3:[{1,8},{2,0x16}]]
>                                  id:5,flag:2,len:4
>                                      081e 100a
>                                      id:1,value:1e
>                                      id:2,value:0a
>                                     +[5:[{1,0x1e},{2,0x0a}]]
> 00000040: 0a06 0800 1000 1800 0a14 0a08 081a 1053  ...............
>          [                  ]
>          id:1,flag:2,len:6
>          2<=[1:[{1,0},{2,0},{3,0}]]
>                              [
>                              id:1,flag:2,len:0x14(20)
                               3<=[1:
>                                    id:1,flag:2,len:8
>                                         [1:[{1,0x1a},{2,0x53},{3,0x01},{4,0x0a}]
> 00000050: 1801 200a 1208 082e 1058 1801 200a ----  .. ......X.. ...
>                    ]
>                     id:2,flag:2,len:8
                           [                 ]
>                          [2:[{1,0x2e},{2,0x58},{3,1},{4,0x0a}]]
> 00000050: ---- ---- ---- ---- ---- ---- ---- 1208  .. ......X.. ...
>                                              id:2,flag:2,len:8
> 00000060: 0822 102a 180b 2007 0000 0000 b03c 0000  .".*.. ......<..
>          [                   ]
>          id:1,0x22
>          id:2,0x2a
>          id:3,0x0b
>          id:4,0x07
>          5<=[2:[{1,0x22},{2,0x2a},{3,0x0b},{4,0x07}]]
>                               0
>                                         15536
> 00000070: 0a3d 0000 643d 0000 be3d 0000 183e 0000  .=..d=...=...>..
> 00000080: 723e 0000 cc3e 0000 263f 0000 803f 0000  r>...>..&?...?..
> 00000090: da3f 0000 3440 0000 dd40 0000 8641 0000  .?..4@...@...A..
> 000000a0: 2f42 0000 d842 0000 8143 0000 2a44 0000  /B...B...C..*D..

### bg_only_packed.bin

#### file size

* 3cf0

#### header

> 00000000: 484d 4449 414c 00ff ffff ffff ffff ffff  HMDIAL..........
> 00000010: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000020: 5901 0000 0c00 0000 0a04 0808 1001 1204  Y...............
>                               id:1,flag:2
>                               len(4)
>                                    08 08 10 01
>                                    id:1,value:8
>                                    id:2,value:1
>                              (1)[parameter descriptor] parameterTableLength:8, imageCount:1
>                                              id:2,flag:2
>                                               len(4)
>                                           (2)[Watch face parameters locations]
> 00000030: 0800 1008 0a06 0800 1000 1800 0000 0000  ................
>           0800 1008
>           id:1,value:0
>           id:2,value:8
>           [2:[{1,0},{2,8}]]
>                     (3)[                  ] <- parametersStream in readParameters
>                     id:1,flag:2
>                     len(6)
>                          0800 1000 1800
>                          id:1,value:0
>                          id:2,value:0
>                          id:3,value:0
                           [{1,0},{2,0},{3,0}] -> Parameter(2, {}) -> _parameters

#### image section

> 00000040: 424d 6400 b000 b000 5800 0400 0800 0000  BMd.....X.......
>           [HEADER ] [wdh][hgt][rLn][BPP][pal]
> 00000050: 0000 0000 0000 ff00 00ff 0000 00ff ff00  ................

> 2019-07-28 19:29:06,429 - root - INFO - Width: 176, Height: 176, RowLength: 88
> 2019-07-28 19:29:06,429 - root - INFO - BPP: 4, PaletteColors: 8, Transparency: False
> 2019-07-28 19:29:06,429 - root - INFO - Reading palette...
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 0: R  0, G  0, B  0
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 1: R  0, G  0, B FF
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 2: R  0, G FF, B  0
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 3: R  0, G FF, B FF
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 4: R FF, G  0, B  0
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 5: R FF, G  0, B FF
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 6: R FF, G FF, B  0
> 2019-07-28 19:29:06,429 - root - INFO - Palette item 7: R FF, G FF, B FF

## by crystal tile 2

### 2eac844-48-4e4254dc71

#### file size

* acd77

#### common header(?)

> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6bea 0000 7c3e ffff ffff ffff ffff   .k...|>........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5a00 0000

#### header

> 00000030:                     1200 0000 4000 0000  ....Z.......@...
>                               Unknown   ParamSize
> 00000040: 0a04 0874 1007 1204 0800 101a 5204 081a  ...t........R...
>           id:1,flag:2,len:4
>               [         ]
>                0874 1007
>                id:1,value:0x74
>                id:2,value:7
>                (1)[parameter descriptor] parameterTableLength:116, imageCount:7
>                          id:2,flag:2,len:4
>                               [        ]
>                               0800 101a
>                               id:1,value:0x0
>                               id:2,value:0x1a
>                               [2:[{1,0},{2,0x1a}]]
>                                         id:10,flag:2,len:4
>                                               081a
> 00000050: 105a
>                                         +[10:[{1,0x1a},{2,0x5a}]]
> 00000050: ---- 0a06 0800 1000 1800 1a06 0800 1000  .Z..............
>                id:1,flag:2,len:6
>                     [             ]
>                     id:1,value:0
>                     id:2,value:0
>                     id:3,value:0
>                                    id:3,flag:2,len:6
>                                         id:1,0
>                                         2,0
> 00000060: 1801
>           3,1
> 00000060: ---- 2208 08a7 0110 a801 1802 0a18 0800  ..".............
>                id:4,flag:2,len:8
>                     id:1, val:167
>                     id:2, val:168
>                     id:3, val:2
>                                         id:1,flag:2,len:0x18
>                                              id:1,val:0
> 00000070: 1000 1a04 0800 1000 2204 0800 1000 2a06  ........".....*.
>           id:2,val:0
>           id:3,flag:2,len:4
>                     id:1,val:0
>                     id:2.val:0
>                               id:4,flag:2,len:4
>                                    id:1,0
>                                    id:2,0
>                                              id:5,flag:2,ken:6
> 00000080: 0803 1076 1803 1219 0800 1000 1a04 0800  ...v............
>           id:1,val:3
>           id:2,val:0x76
>           id:3,val:0x03
>
> 00000090: 1000 2204 0800 1000 2a07 0802 1098 0118  ..".....*.......
> 000000a0: 041a 1908 0010 001a 0408 0010 0022 0408  ............."..
> 000000b0: 0010 002a 0708 0110 9c01                 ...*........"...

> 000000b0:                          1805 2208 08af  ...*........"...
> 000000c0: 0110 af01 1806 0200 0000 5ef4 0700 86a5  ..........^.....
> 000000d0: 0a00 2eb0 0a00 9ebb 0a00 56c5 0a00 eeca  ..........V.....
> 000000e0: 0a00 ffff

#### image section
> 000000e0: ---- ---- 424d ffff 6901 0000 6901 0000  ....BM..i...i...
> 000000f0: 2000 0000 1800 0000 0100 0000 2929 2900   ...........))).
>                     [HEADER ] [wdh     ][hgt     ]
>           [bpp     ][?     ][?     ]

* https://amazfitwatchfaces.com/verge-lite/view/5
* simple analog watchface
* 32bit BGR-a(?)

| h_offset | dim | c_offset | description |
|---|---|---|---|
| e4 | 0x169 x 0x169 (361x361) | fc | bg |
| 7f540 | 0xd2 x 0xd2 (210x210) | 7f558 | preview  |
| aa668 | 0x1a x 0x1a (26x26) | aa680 | center image? |
| ab110 | 0x06 x 0x79 (6x121) | ab128 | hour hand |
| abc80 | 0x04 x 0x9a (4x154) | abc98 | min hand |
| ac638 | 0x02 x 0xb0 (2x176) | ac650 | sec hand |
| acbd0 | 0x0a x 0x0a (10x10) | acbe8 | sec center |

* acbd0 42 4d ff ff 0a 00 00 00 0a 00 00 00 20 00 00 00
* 18 00 00 00 01 00 00 00

### 6d11de-48-50a39f979f

#### file size

* 13420f

#### common header(?)

> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6cea 0000 3f2c ffff ffff ffff ffff   .l...?,........
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 5000 0000 

* https://amazfitwatchfaces.com/verge-lite/view/8
* simple analog watchface w/ weekday, day
* 32bit BGR-a(?)

| h_offset | dim | c_offset | description |
|---|---|---|---|
| 148 | 0x168 x 0x168 (360x360) | 160 | bg |
| 7ea60 | 0xd2 x 0xd2 (210x210) | 7ea7c | preview  |
| a9b88 | 0x15d x 0x15c (349x348) | a9ba0 | dial  |
| 120550 | 0x11 x 0x11 (17x17) | 120568 | date 0  |
| 1209ec | 0x11 x 0x11 () | 120a04 |   |
| 120e88 | 0x11 x 0x11 () | 120ea0 |   |
| 121324 | 0x11 x 0x11 () | 12133c |   |
| 1217c0 | 0x11 x 0x11 () | 1217d8 |   |
| 121c5c | 0x11 x 0x11 () | 121c74 |   |
| 1220f8 | 0x11 x 0x11 () | 122110 |   |
| 122594 | 0x11 x 0x11 () | 1225ac |  |
| 122a30 | 0x11 x 0x11 () | 122a48 |  |
| 122ecc | 0x11 x 0x11 () | 122ee4 | date 9 |
| 123368 | 0x37 x 0x11 (55x17) | 123380 | mon |
| 12421c | 0x37 x 0x11 () | 124234 | tue |
| 1250d0 | 0x37 x 0x11 () | 1250e8 | wed |
| 125f84 | 0x37 x 0x11 () | 125f9c | thu |
| 126e38 | 0x29 x 0x11 (41x17) | 126e50 | fri |
| 127934 | 0x36 x 0x11 (54x17) | 12794c | sat |
| 1287a4 | 0x37 x 0x11 (55x17) | 1287bc | sun |
| 129658 | 0x1e x 0x74 (30x116) | 129670 | hour hand |
| 12ccd0 | 0x18 x 0x99 (24x153) | 12cce8 | min hand |
| 130648 | 0x14 x 0xbf (20x191) | 130660 | sec hand |

### d126a9f-48-2a91eb35b2

#### file size

* d5e83

#### common header(?)

> 00000000: 484d 4449 414c 00ff ffff ff06 ffff ffff  HMDIAL..........
> 00000010: 2000 6fea 0000 14de ffff ffff ffff ffff   .o.............
> 00000020: ffff ffff ffff ffff ffff ffff ffff ffff  ................
> 00000030: ffff ffff 3a00 0000

* https://amazfitwatchfaces.com/verge-lite/view/6
* digital watch w/ battery, heartbeat, steps, weekday, date
* 32bit RGB-a

#### image section
> 000001e0: ---- ---- 424d ffff 6801 0000 6801 0000  Y...BM..h...h...
> 000001f0: 2000 0000 1800 0000 0100 0000 0000 0000   ...............

| h_offset | dim | c_offset | description |
|---|---|---|---|
| 1e4 | 0x168 x 0x168 (360x360) | 1fc | bg |
| 7eafc | 0xd2 x 0xd2 (210x210) | 7eb14 | preview |
| a9c24 | 0x28 x 0x56 (40x86) | a9c3c | hhmm 0 |
| ad1fc | 0x28 x 0x56 () | ad214 | hhmm 1 |
| b07d4 | 0x28 x 0x56 () | b07ec | hhmm 2 |
| b3dac | 0x28 x 0x56 () | b3dc4 | hhmm 3 |
| b7384 | 0x28 x 0x56 () | b739c | hhmm 4 |
| ba95c | 0x28 x 0x56 () | ba974 | hhmm 5 |
| bdf34 | 0x28 x 0x56 () | bdf4c | hhmm 6 |
| c150c | 0x28 x 0x56 () | c1524 | hhmm 7 |
| c4ae4 | 0x28 x 0x56 () | c4afc | hhmm 8 |
| c80bc | 0x28 x 0x56 () | c80d4 | hhmm 9 |
| cb694 | 0x06 x 0x0e (6x14) | cb6ac | small 0 |
| cb7fc | 0x06 x 0x0e () | cb814 | |
| cb964 | 0x06 x 0x0e () | cb97c | |
| cbacc | 0x06 x 0x0e () | cbae4 | |
| cbc34 | 0x06 x 0x0e () | cba4c | |
| cbd9c | 0x06 x 0x0e () | cbdb4 | |
| cbf04 | 0x06 x 0x0e () | cbf1c | |
| cc06c | 0x06 x 0x0e () | cc084 | |
| cc1d4 | 0x06 x 0x0e () | cc1ec | |
| cc33c | 0x06 x 0x0e () | cc354 | small 9 |
| cc4a4 | 0x06 x 0x0e () | cc4bc | small dot |
| cc60c | 0x20 x 0x0e (32x14) | cc624 | mon |
| ccd24 | 0x20 x 0x0e () | ccd3c | tue |
| cd43c | 0x20 x 0x0e () | cd454 | wed |
| cdb54 | 0x20 x 0x0e () | cdb6c | thur |
| ce26c | 0x20 x 0x0e () | ce284 | fri |
| ce984 | 0x20 x 0x0e () | ce99c | sat |
| cf09c | 0x20 x 0x0e () | cf0b4 | sun |
| cf7b4 | 0x50 x 0x50 (80x80) | cf7cc | circle of battery? |
| d5bcc | 0x0c x 0x0e (12x14) | d5be4 | small percent |

* d5bcc 42 4d ff ff
* 0c 00 00 00 0e 00 00 00 20 00 00 00 18 00 00 00
* 01 00 00 00