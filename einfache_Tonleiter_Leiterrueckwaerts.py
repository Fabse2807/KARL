from karl.v2 import *

for i in range (0,12):
    speaker.beep(0.5,i)
    
for i in range (12,0,-1):
    speaker.beep(0.5,i)