from karl.v2 import *
def move ():
    
    right_foot.angle(30)
    sleep(1)
    left_foot.angle(30)
    sleep(2)
    right_foot.angle(0)
    left_foot.angle(0)
    right_foot.angle(30)
    sleep(1)
    left_foot.angle(-30)
    sleep(2)
    right_foot.angle(0)
    left_foot.angle(0)
    sleep(1)
    right_leg.angle(-30)
    sleep(1)
    left_leg.angle(20)
    sleep(2)
    right_leg.angle(0)
    left_leg.angle(0)
    sleep(2)
    
move()
move()
move()