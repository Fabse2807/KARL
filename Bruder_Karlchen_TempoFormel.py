from karl.v2 import *

tempo = 120
viertel = 0.25*tempo/60
halbe = viertel *2
achtel = viertel /2

def move ():
    right_foot.angle(30)
    sleep(1)
    left_foot.angle(-30)
    sleep(2)
    right_foot.angle(0)
    left_foot.angle(0)

def blink ():
    left_eye.red.on()
    sleep(0.5)
    left_eye.red.off()
    right_eye.green.on()
    sleep(0.5)
    right_eye.green.off()
    right_eye.blue.on()
    sleep(0.5)
    right_eye.blue.off()

for i in range(2):
    speaker.beep(viertel, 0)
    speaker.beep(viertel, 2)
    speaker.beep(viertel, 4)
    speaker.beep(viertel, 0)

blink()
move()
blink()

for j in range(2):
    speaker.beep(viertel, 4)
    speaker.beep(viertel, 5)
    speaker.beep(halbe, 7)

blink()
blink()

for k in range(2):
    speaker.beep(achtel, 7)
    speaker.beep(achtel, 9)
    speaker.beep(achtel, 7)
    speaker.beep(achtel, 5)
    speaker.beep(viertel, 4)
    speaker.beep(viertel, 0)

move()
blink()
blink()

for l in range(2):
    speaker.beep(viertel, 0)
    speaker.beep(viertel, -5)
    speaker.beep(viertel, 0)