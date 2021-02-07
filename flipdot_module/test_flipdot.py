#!/usr/bin/python3
#
# Test flipdot module

import flipdot

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

flipdot.display()

flipdot.reset(True)

flipdot.display()