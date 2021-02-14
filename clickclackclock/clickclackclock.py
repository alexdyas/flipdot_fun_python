#!/usr/bin/python3
#
# Click Clack Clock

import flipdot
from datetime import datetime

flipdot = flipdot.Flipdot('/dev/ttyUSB0',57600)

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
hour = now.strftime("%H")
minute = now.strftime("%M")
print("date and time ="+hour+":"+minute)

flipdot.reset(False)
flipdot.text_letter('1',0)

flipdot.display()

flipdot.dumpdisplaybuffer()
