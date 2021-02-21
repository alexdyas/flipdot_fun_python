#!/usr/bin/python3

import flipdot

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

message = "Hello World"


flipdot.message("setno1",message)