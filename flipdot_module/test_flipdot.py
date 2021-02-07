#!/usr/bin/python3
#
# Test flipdot module

import flipdot
import time

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

state = True

while True:

  flipdot.display()

  flipdot.reset(state)

  state = not state

  time.sleep(1)