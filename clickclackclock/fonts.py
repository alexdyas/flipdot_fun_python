# Fonts class
class Fonts :

  simple =  { '1' : [ [0,0,1,0,0],
                      [0,1,1,0,0],
                      [1,0,1,0,0],
                      [0,0,1,0,0],
                      [0,0,1,0,0],
                      [0,0,1,0,0],
                      [1,1,1,1,1]
                    ],

              '2' : [ [0,1,1,1,0],
                      [1,0,0,0,1],
                      [0,0,0,0,1],
                      [0,0,1,1,0],
                      [0,1,0,0,0],
                      [1,0,0,0,0],
                      [1,1,1,1,1]
                    ],
              '3' : [ [0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,1,1,0],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                  ],

              '4' : [  [0,0,0,1,0],
                    [0,0,1,1,0],
                    [0,1,0,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0]
                    ],

              '5' : [  [1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                    ],

              '6' : [  [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                    ],

              '7' : [  [1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]
                    ],

              '8' : [  [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                    ],

              '9' : [  [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                    ],

              '0' : [  [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,1,1],
                    [1,0,1,0,1],
                    [1,1,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]
                    ]
              }



#  def __init__(self):
#    print("Init")

  def character(self,font,character):
    return self.simple[character]


# # Letters
# old_letters = { 'A' : [0x7e,0x7f,0x09,0x09,0x7f,0x7e],
#             'B' : [0x7f,0x7f,0x49,0x49,0x7f,0x36],
#             'C' : [0x3e,0x7f,0x41,0x41,0x63,0x22],
#             'D' : [0x7f,0x7f,0x41,0x41,0x7f,0x3e],
#             'E' : [0x7f,0x7f,0x49,0x49,0x49,0x41],
#             'F' : [0x7f,0x7f,0x09,0x09,0x09,0x01],
#             'G' : [0x3e,0x7f,0x41,0x51,0x73,0x32],
#             'H' : [0x7f,0x7f,0x08,0x08,0x7f,0x7f],
#             'I' : [0x00,0x41,0x7f,0x7f,0x41,0x00],
#             'J' : [0x30,0x70,0x41,0x7f,0x3f,0x01],
#             'K' : [0x7f,0x7f,0x1c,0x36,0x63,0x41],
#             'L' : [0x7f,0x7f,0x40,0x40,0x40,0x40],
#             'M' : [0x7f,0x7f,0x06,0x0c,0x06,0x7f,0x7f],
#             'N' : [0x7f,0x7f,0x06,0x0c,0x18,0x7f,0x7f],
#             'O' : [0x3e,0x7f,0x41,0x41,0x7f,0x3e,0x00],
#             'P' : [0x7f,0x7f,0x11,0x11,0x1f,0x0e],
#             'Q' : [0x1e,0x3f,0x21,0x31,0x7f,0x5e],
#             'R' : [0x7f,0x7f,0x19,0x39,0x6f,0x46],
#             'S' : [0x26,0x6f,0x49,0x49,0x7b,0x32],
#             'T' : [0x03,0x01,0x7f,0x7f,0x01,0x03],
#             'U' : [0x3f,0x7f,0x40,0x40,0x7f,0x7f],
#             'V' : [0x1f,0x3f,0x60,0x60,0x3f,0x1f],
#             'W' : [0x7f,0x7f,0x30,0x18,0x30,0x7f,0x7f],
#             'X' : [0x63,0x77,0x1c,0x08,0x1c,0x77,0x63],
#             'Y' : [0x07,0x0f,0x78,0x78,0x0f,0x07],
#             'Z' : [0x61,0x71,0x59,0x4d,0x47,0x43],
#             'a' : [0x20,0x74,0x54,0x54,0x7c,0x78],
#             'b' : [0x7f,0x7f,0x48,0x48,0x78,0x30],
#             'c' : [0x38,0x7c,0x44,0x44,0x6c,0x28],
#             'd' : [0x30,0x78,0x48,0x48,0x7f,0x7f],
#             'e' : [0x38,0x7c,0x54,0x54,0x5c,0x18],
#             'f' : [0x10,0x7e,0x7f,0x11,0x13,0x02],
#             'g' : [0x0c,0x5e,0x52,0x52,0x7e,0x3e],
#             'h' : [0x7f,0x7f,0x08,0x08,0x78,0x70],
#             'i' : [0x00,0x40,0x7a,0x7a,0x40,0x00],
#             'j' : [0x30,0x70,0x40,0x7d,0x3d,0x00],
#             'k' : [0x7f,0x7f,0x10,0x38,0x6c,0x44],
#             'l' : [0x00,0x00,0x7f,0x7f,0x00,0x00],
#             'm' : [0x7c,0x7c,0x18,0x70,0x18,0x7c,0x7c],
#             'n' : [0x7c,0x7c,0x0c,0x0c,0x7c,0x78],
#             'o' : [0x38,0x7c,0x44,0x44,0x7c,0x38],
#             'p' : [0x7e,0x7e,0x12,0x12,0x1e,0x0c],
#             'q' : [0x0c,0x1e,0x12,0x7e,0x7e,0x40,0x60],
#             'r' : [0x7c,0x7c,0x04,0x04,0x1c,0x18],
#             's' : [0x48,0x54,0x54,0x54,0x54,0x24],
#             't' : [0x08,0x08,0x7e,0x7e,0x08,0x08],
#             'u' : [0x3c,0x7c,0x40,0x40,0x7c,0x7c],
#             'v' : [0x18,0x38,0x60,0x60,0x38,0x18],
#             'w' : [0x3c,0x7c,0x40,0x78,0x40,0x7c,0x3c],
#             'x' : [0x44,0x6c,0x38,0x38,0x6c,0x44],
#             'y' : [0x0c,0x5c,0x50,0x50,0x7c,0x3c],
#             'z' : [0x00,0x64,0x74,0x5c,0x4c,0x00],
#             '1' : [0x40,0x44,0x7f,0x7f,0x40,0x40],
#             '2' : [0x62,0x73,0x51,0x49,0x4f,0x46],
#             '3' : [0x22,0x63,0x49,0x49,0x7f,0x36],
#             '4' : [0x18,0x14,0x12,0x7f,0x7f,0x10],
#             '5' : [0x27,0x67,0x45,0x45,0x7d,0x39],
#             '6' : [0x3e,0x7f,0x49,0x49,0x7b,0x32],
#             '7' : [0x03,0x03,0x71,0x7d,0x0f,0x03],
#             '8' : [0x36,0x7f,0x49,0x49,0x7f,0x36],
#             '9' : [0x26,0x6f,0x49,0x49,0x7f,0x3e],
#             '0' : [0x3e,0x7f,0x49,0x45,0x7f,0x3e]
#           }
