#!/usr/bin/python3
#
# Click Clack Clock

import flipdot
from datetime import datetime
import time

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

# datetime object containing current date and time


while True :
  now = datetime.now()

  hour = now.strftime("%H")
  minute = now.strftime("%M")

  flipdot.text_letter(hour[0],0)
  flipdot.text_letter(hour[1],6)
  flipdot.text_letter(minute[0],12)
  flipdot.text_letter(minute[1],18)
  flipdot.display()
  time.sleep(1)



#flipdot.reset(False)
#for number in range(0,10) :
#  flipdot.text_letter(str(number),0)
#  time.sleep(1)
#  flipdot.display()
