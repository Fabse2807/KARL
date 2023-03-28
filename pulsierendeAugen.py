from karl.v2 import *

for i in range(0, 256):
    left_eye.intensity(i)
    right_eye.intensity(i)
    sleep(0.05)
    
print(i)

for i in range(255,-1,-1):
    print(i)
    left_eye.intensity(i)
    right_eye.intensity(i)
    sleep(0.05)
