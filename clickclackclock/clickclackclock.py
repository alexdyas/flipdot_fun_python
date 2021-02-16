#!/usr/bin/python3
#
# Click Clack Clock

import flipdot
from datetime import datetime
import time

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
hour = now.strftime("%H")
minute = now.strftime("%M")
print("date and time ="+hour+":"+minute)

flipdot.reset(False)
for number in range(0,10) :
  flipdot.text_letter(str(number),0)
  time.sleep(1)
  flipdot.display()
