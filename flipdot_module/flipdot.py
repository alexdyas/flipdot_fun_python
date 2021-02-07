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
    displaybuffer[x][y] = state

  # Flip the dot at x,y. White becomes black, visa versa
  def reversedot(self,x,y):
    displaybuffer[x][y] = not display[x][y]

  # Set the whole buffer to On or Off
  def reset(self,state):
    displaybuffer = [[state for x in range(width)] for y in range(height)]

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

      # Translate binary to hex
      #hexvalue = hex(int(binarystring, 2))

      # Debug
      self.displaybytearray.append(0x02)

    # End of transmission byte
    self.displaybytearray.append(0x8F)

    # Throw it all down the pipe
    self.serialPort.write(self.displaybytearray)

  # Debug routine to dump contents of internal display buffer to stdout
  def dumpdisplaybuffer(self):
    for y in range(self.displayHeight) :
      for x in range(self.displayWidth) :
        print(self.displaybuffer[y][x],end='')
      print()