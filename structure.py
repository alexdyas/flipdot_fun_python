#!/usr/bin/python3
#


# letters = { 'A' : [0x7e,0x7f,0x09,0x09,0x7f,0x7e],
#               'B' : [0x7f,0x7f,0x49,0x49,0x7f,0x36],
#               'C' : [0x3e,0x7f,0x41,0x41,0x63,0x22],



# characters =  [ [ [0,0,1,0,0],
#                     [0,1,1,0,0],
#                     [1,0,1,0,0],
#                     [0,0,1,0,0],
#                     [0,0,1,0,0],
#                     [0,0,1,0,0],
#                     [1,1,1,1,1]
#                   ],

#   char_2 = {  {0,1,1,1,0},
#                     {1,0,0,0,1},
#                     {0,0,0,0,1},
#                     {0,0,1,1,0},
#                     {0,1,0,0,0},
#                     {1,0,0,0,0},
#                     {1,1,1,1,1} };

#             ]


all_characters =  { '1' : [ [0,0,1,0,0],
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
                          ]
                  }


print(all_characters["1"][0][0])