#The position and number of hurdles changes each time this world is reloaded.Folow the direction
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
    #if front_is_clear()==True:
        move()
    elif wall_in_front():
    #elif wall_in_front()==True:
    #else:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left() # it is an important step because the robot should look at | instead of __ to make wall_in_front function work perfectly!
