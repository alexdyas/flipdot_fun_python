#!/usr/bin/python3
#
# Click Clack Clock

import flipdot
from datetime import datetime
import time

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

# datetime object containing current date and time

#flipdot.reset(False)
#flipdot.display()

while True :
  now = datetime.now()

  hour = now.strftime("%H")
  minute = now.strftime("%M")

  flipdot.text_letter("setno1",hour[0],0)
  flipdot.text_letter("setno1",hour[1],7)
  flipdot.text_letter("setno1",minute[0],15)
  flipdot.text_letter("setno1",minute[1],22)

  # !! Only send if time has changed

  flipdot.display()
  time.sleep(1)



#flipdot.reset(False)
#for number in range(0,10) :
#  flipdot.text_letter(str(number),0)
#  time.sleep(1)
#  flipdot.display()
