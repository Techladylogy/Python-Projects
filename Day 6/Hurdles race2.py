#Stopping at a flag (random position)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_set():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()    
#negation
while not at_goal():
  jump_set()

#while at_goal() != True:
    #jump_set()
