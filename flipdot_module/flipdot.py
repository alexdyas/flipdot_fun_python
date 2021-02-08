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
  displaybytearray = bytearray([])

  font = {
      ' ': bytearray([0]),
      '+': bytearray([24,  126, 126,  24,  0]),
      '-': bytearray([24,   24,  24,  24,  0]),
      '0': bytearray([62,   65,  65,  62,  0]),
      '1': bytearray([0,   66,  127, 64,  0]),
      '2': bytearray([98,   81,  73,  70,  0]),
      '3': bytearray([34,   65,  73,  54,  0]),
      '4': bytearray([56,   36,  34, 127, 32]),
      '5': bytearray([79,   73,  73,  49,  0]),
      '6': bytearray([62,   73,  73,  50,  0]),
      '7': bytearray([3,    1,   1, 127,  0]),
      '8': bytearray([54,   73,  73,  54,  0]),
      '9': bytearray([38,   73,  73,  62,  0]),
      'A': bytearray([0x3C, 0x0A, 0x0A, 0x3C]),
      'B': bytearray([0x3E,0x2A,0x2A,0x14]),
      'C': bytearray([0x1C,0x22,0x22,0x14]),
      'D': bytearray([0x3E,0x22,0x22,0x1C]),
      'E': bytearray([0x3E,0x2A,0x2A]),
      'F': bytearray([0x3E,0x0A,0x0A]),
      'G': bytearray([0x1C,0x22,0x2A,0x2A]),
      'H': bytearray([0x3E,0x08,0x08,0x3E]),
      'I': bytearray([0x3E]),
      'J': bytearray([0x10,0x20,0x20,0x1E]),
      'K': bytearray([0x3E, 0x08, 0x14, 0x22]),
      'L': bytearray([0x3E,0x20,0x20]),
      'M': bytearray([0x3E,0x04,0x08,0x04]),
      'N': bytearray([0x3E,0x04,0x08,0x3E]),
      'O': bytearray([0x1C,0x22,0x22,0x1C]),
      'P': bytearray([0x3E,0x0A,0x0A,0x1C,0x04]),
      'Q': bytearray([0x1C,0x22,0x12,0x2C]),
      'R': bytearray([0x3E,0x0A,0x1A,0x24]),
      'S': bytearray([0x24,0x2A,0x2A,0x12]),
      'T': bytearray([0x02,0x02,0x3E,0x02,0x02]),
      'U': bytearray([0x1E,0x20,0x20,0x1E]),
      'V': bytearray([0x06,0x18,0x20,0x18,0x6]),
      'W': bytearray([0x1E,0x20,0x1E,0x20,0x1E]),
      'X': bytearray([0x36,0x08,0x08,0x36]),
      'Y': bytearray([0x2E,0x28,0x28,0x1E]),
      'Z': bytearray([0x32,0x2A,0x2A,0x26])
  }

  # Constructor
  def __init__(self,passed_serialPortDevice,passed_serialBaudrate):

    self.serialPortDevice = passed_serialPortDevice
    self.serialBaudrate = passed_serialBaudrate

    self.serialPort = serial.Serial(self.serialPortDevice,self.serialBaudrate)

    if self.serialPort.isOpen() :
      self.serialPort.close()
    self.serialPort.open()

    # Initialise the display 2D 'array' (Actually list of lists)
    self.displaybuffer = [[False for x in range(self.displayWidth)] for y in range(self.displayHeight)]

  # Set dot at x,y
  def setdot(self,x,y,state):
    self.displaybuffer[x][y] = state

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
        if self.displaybuffer[y][x] :
          binarystring = binarystring + '1'
        else:
          binarystring = binarystring + '0'

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

  def write(self,letter) :
    print("Complete me")

  def character(self,character) :


  # Debug routine to dump contents of internal display buffer to stdout
  def dumpdisplaybuffer(self):
    for y in range(self.displayHeight) :
      for x in range(self.displayWidth) :
        print(self.displaybuffer[y][x],end='')
      print()