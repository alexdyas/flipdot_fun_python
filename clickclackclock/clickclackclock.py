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

flipdot.text_letter('1',0)
flipdot.text_letter('2',7)
flipdot.text_letter('3',14)
flipdot.text_letter('4',21)

flipdot.display_raw()