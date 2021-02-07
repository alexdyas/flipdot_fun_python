#!/usr/bin/python3
#
# Test flipdot module

import flipdot
import time
import random

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

flipdot.randomfade(True)