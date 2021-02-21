#!/usr/bin/python3


# Zip

from pprint import pprint
import fonts
thefonts = fonts.Fonts()

A = thefonts.character("setno1","A")
space = thefonts.character("setno1"," ")
B = thefonts.character("setno1","B")

combined = zip(A,space,B,A,space,B,A)

for element1 in combined :
  print(element1[1])