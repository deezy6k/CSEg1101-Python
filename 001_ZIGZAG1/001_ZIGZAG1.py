'''
PROGRAM => ZIGZAG1* Solution
Author => Dawit K.
'''

from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.05)

#This function makes hubo move 9 times in the current direction 
def move_nine_steps():
    for i in range(9):
        hubo.move()
        
#This function makes hubo turn to right direction by turning left 3 times         
def turn_right():
    for i in range(3):
        hubo.turn_left()

#This function allows hubo to move up 9 steps and down 9 steps          
def move_up_down():
    move_nine_steps()
    turn_right()
    hubo.move()
    turn_right()
    move_nine_steps()

#This function allows hubo to rearrange its pos and directon for next move   
def arrange_pos():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    
hubo.turn_left()
for i in range(4):
    move_up_down()
    arrange_pos()
move_up_down()

