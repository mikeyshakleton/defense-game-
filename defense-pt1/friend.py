import turtle
import pyautogui

wn = turtle.Screen()
wn.bgcolor("green")
wn_x,wn_y = pyautogui.size()
wn.setup(wn_x,wn_y)

walle = False

block = "block.gif"

wn.register_shape(block)

collider = turtle.Turtle()
collider.shape("circle")
collider.goto(0,0)
collider.shapesize(2,2)
collider.hideturtle()

ant_body = turtle.Turtle()
ant_body.shape("square")
ant_body.color("brown")
ant_body.pu()
ant_body.goto(0,0)
ant_body.shapesize(0.5,0.5)

ant_left1 = turtle.Turtle()
ant_left1.shape("square")
ant_left1.color("brown")
ant_left1.pu()
ant_left1.goto(-10,10)
ant_left1.shapesize(0.5,0.5)

ant_left2 = turtle.Turtle()
ant_left2.shape("square")
ant_left2.color("brown")
ant_left2.pu()
ant_left2.goto(-10,-10)
ant_left2.shapesize(0.5,0.5)

wall = turtle.Turtle()
wall.shape(block)
wall.pu()
wall.goto(0,0)
wall.hideturtle()

print(wall.shapesize())

ant_right1 = turtle.Turtle()
ant_right1.shape("square")
ant_right1.color("brown")
ant_right1.pu()
ant_right1.goto(10,10)
ant_right1.shapesize(0.5,0.5)

ant_right2 = turtle.Turtle()
ant_right2.shape("square")
ant_right2.color("brown")
ant_right2.pu()
ant_right2.goto(10,-10)
ant_right2.shapesize(0.5,0.5)

ant_chest = turtle.Turtle()
ant_chest.shape("square")
ant_chest.color("brown")
ant_chest.pu()
ant_chest.goto(0,0)
ant_chest.shapesize(0.5,0.5)


ant_head = turtle.Turtle()
ant_head.shape("square")
ant_head.color("brown")
ant_head.pu()
ant_head.goto(0,20)
ant_head.shapesize(0.5,0.5)

def click(x,y):
    global walle
    walle = True
    wall.showturtle()
    wall.goto(x,y)
    wall.stamp()

wn.listen()
wn.onclick(click)
running = True

while running:
    wn.update()