#Stopping at a flag (random position)
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
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
