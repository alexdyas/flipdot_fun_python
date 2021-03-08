#!/usr/bin/env python3
# ------------------------------------------------------------------------------
#
# File          - bouncing_ball.py
#
# Description   - Bouncing ball demo - Python version
#
# Find me       - <github>
#
# Author        - Alexander Dyas
#
# ------------------------------------------------------------------------------
import serial
from serial import (
    PARITY_NONE,
    EIGHTBITS,
    STOPBITS_ONE,
)
import sys
import time

# Prepare the serial port
serialPort = serial.Serial('/dev/cu.usbserial-0001')
serialPort.baudrate = 57600
serialPort.parity = PARITY_NONE
serialPort.bytesize = EIGHTBITS
serialPort.stopbits = STOPBITS_ONE
if serialPort.isOpen() :
  print("Port was open, reopening")
  serialPort.close()
serialPort.open()

# Start ball somewhere in the grid
xpos = 1
ypos = 1

# What direction the ball is going in
xdirection = 1
ydirection = 1

# Extents of the flipdot display
xmax = 28
ymax = 7

# Initialise display byte array. The header and end of transmission bytes will never need to be changed, only the display bytes
display_array = bytearray([
    0x80,  # header
    0x83,  # 28 bytes refresh
    0xFF,  # display address, FF == all displays
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 28 bytes data
    0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x8F #EOT
])

ball_position = 0

# Infinite loop
while True:

  # Make all the columns before the ball black
  for count in range(1,xpos,1) :
    display_array[count+2]=0x00

  # Is there a way of calculating this mapping in one line?
  if ypos == 1 :
    ball_position = 0x01
  elif ypos == 2 :
    ball_position = 0x02
  elif ypos == 3 :
    ball_position = 0x04
  elif ypos == 4 :
    ball_position = 0x08
  elif ypos == 5 :
    ball_position = 0x10
  elif ypos == 6 :
    ball_position = 0x20
  elif ypos == 7 :
    ball_position = 0x40
  else :
    print("Got an unsupported xpos, plodding on regardless")
  display_array[xpos+2] = ball_position

  # Make all the columns after the ball black
  for count in range(xpos+1,28,1) :
    display_array[count+3]= 0x00

  # Write array to serial port
  serialPort.write(display_array)

  # Change direction if we've reached a wall
  if xpos == xmax  :
    xdirection = -1
  if xpos == 1 :
    xdirection = 1
  if ypos == ymax :
    ydirection = -1
  if ypos == 1 :
    ydirection = 1

  # Advance ball
  xpos = xpos + xdirection
  ypos = ypos + ydirection

  # Don't go too fast
  time.sleep(.2)
