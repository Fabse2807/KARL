from karl.v2 import *

for i in range (9,2,-2):
    for j in range(8,0,-1):
        speaker.beep(0.5,j)
        
    for k in range(0,8):
        speaker.beep(0.5, k)
    
    