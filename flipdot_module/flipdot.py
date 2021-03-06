# Represents the flipdot display as a matrix 7x28
# 0,0 is the top left hand corner
# 27,6 is the bottom right

# Dots are either True of False, On / Off, Black White

# Most of the methods will not result in anything sent to the display. The display method dumps the internal representation to the display

# Only handles a single 7x28 display as that's all I have at the moment

import serial
from serial import (
    PARITY_NONE,
    EIGHTBITS,
    STOPBITS_ONE,
)
import random
import fonts

# REMOVE LATER
from pprint import pprint

class Flipdot:

  # Class attributes

  # Display dimensions
  displayWidth=28
  displayHeight=7

  # Serial
  serialPortDevice = ''
  serialBaudrate = 0

  # Internal matrix to represent display
  displaybuffer = []

  # Byte array that will actually be sent to the serial port
  displaybytearray = bytearray([
      0x80,  # header
      0x83,  # 28 bytes refresh
      0xFF,  # display address, FF == all displays
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 28 bytes data
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x8F #EOT
  ])

  thefonts = fonts.Fonts()

  # Constructor
  def __init__(self,passed_serialPortDevice,passed_serialBaudrate):

    self.serialPortDevice = passed_serialPortDevice
    self.serialBaudrate = passed_serialBaudrate

    self.serialPort = serial.Serial(self.serialPortDevice,self.serialBaudrate)

    if self.serialPort.isOpen() :
      self.serialPort.close()
    self.serialPort.open()

    # Initialise the display 2D 'array' (Actually list of lists)
    self.displaybuffer = [[0 for x in range(self.displayWidth)] for y in range(self.displayHeight)]

  # Set dot at x,y
  def setdot(self,x,y,state):
    self.displaybuffer[y][x] = state

  # Flip the dot at x,y. White becomes black, visa versa
  def reversedot(self,x,y):
    self.displaybuffer[x][y] = not self.displaybuffer[x][y]

  # Set the whole buffer to On or Off
  def reset(self,state):
    self.displaybuffer = [[state for x in range(self.displayWidth)] for y in range(self.displayWidth)]

  # Dump the internal buffer to the display by converting it to bytearray and
  # then push it out the serial port
  def display(self):
    # Header bytes
    self.displaybytearray = bytearray([
      0x80,  #header
      0x83,  # 28 bytes refresh
      0xFF,  # address
    ])

    # Step through the displaybuffer, one column at a time, converting each string of
    # 7 bits to a hex value
    for x in range(self.displayWidth) :
      binarystring = ''
      for y in range(self.displayHeight) :
        if self.displaybuffer[y][x] == 1 :
          binarystring = '1' + binarystring
        else:
          binarystring = '0' + binarystring

      # Translate binary to integer value
      self.displaybytearray.append(int(binarystring, 2))

    # End of transmission byte
    self.displaybytearray.append(0x8F)

    # Throw it all down the pipe
    self.serialPort.write(self.displaybytearray)

  def randomfade(self,state) :
    randomlist=[]
    for x in range(self.displayHeight) :
      for y in range(self.displayWidth) :
        randomlist.append([x,y])
    random.shuffle(randomlist)
    for item in randomlist:
      self.setdot(item[0],item[1],True)
      self.display()

  # Print letter at pos
  def text_letter(self,font,letter,pos) :
    character = self.thefonts.character(font,letter)
    for y in range(len(character)):
      for x in range(len(character[y])) :
        self.displaybuffer[y][x+pos]=character[y][x]

  # Scroll message from right to left
  def message(self,font,message) :

    # Construct 'array' of letters
    messagebuffer = []
    for character in message :
      characterarray=self.thefonts.character(font,character)
      for y in range(len(characterarray)):
        for x in range(len(characterarray[y])):
          messagebuffer[y][x]=characterarray[y][x]

    # Print message one column at a time
    # for column in len(messagebuffer) :
    #   print("Something")

    print(messagebuffer)
    print(len(messagebuffer))
    print(self.displaybuffer)

  # Shift whole display by amount. Positive shifts left to right, negative
  #  right to left. Wrap around.
  def shift(self,amount) :
    print("Complete me")

  # Debug routine to dump contents of internal display buffer to stdout
  def dumpdisplaybuffer(self):
    for y in range(self.displayHeight) :
      for x in range(self.displayWidth) :
        if self.displaybuffer[y][x] :
          print(1,end='')
        else :
          print(0,end='')
      print()