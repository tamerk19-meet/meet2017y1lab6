def up():
    global direction
    direction=UP
    print('you pressed up')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
def left():
    global direction
    direction=LEFT
    print('you pressed left')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-10,y)
    print(turtle.pos())
def down():
    global direction
    direction=DOWN
    print('you pressed down')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y-10)
    print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    print('you pressed right')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+10,y)
    print(turtle.pos())
###################################################
import turtle
turtle.shape('turtle')
UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
SPACEBAR='space'

UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP



turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(turtle.stamp,SPACEBAR)
turtle.listen()
turtle.mainloop()
