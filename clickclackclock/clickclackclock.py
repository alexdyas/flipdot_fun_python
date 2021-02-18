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


# flipdot.text_letter("setno1","O",0)
# flipdot.text_letter("setno1","l",7)
# flipdot.text_letter("setno1","i",10)
# flipdot.text_letter("setno1","v",14)
# flipdot.display()

lasthour = "00"
lastminute = "00"

while True :
  now = datetime.now()

  hour = now.strftime("%H")
  minute = now.strftime("%M")

  if hour != lasthour :
    flipdot.text_letter("setno1",hour[0],0)
    flipdot.text_letter("setno1",hour[1],7)
    flipdot.display()

  if minute != lastminute :
    flipdot.text_letter("setno1",minute[0],15)
    flipdot.text_letter("setno1",minute[1],22)
    flipdot.display()

  # !! Only send if time has changed
  time.sleep(1)

  lasthour = hour
  lastminute = minute


#flipdot.reset(False)
#for number in range(0,10) :
#  flipdot.text_letter(str(number),0)
#  time.sleep(1)
#  flipdot.display()
