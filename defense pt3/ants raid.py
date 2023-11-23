import turtle
import pyautogui
import random
import webbrowser
from PIL import Image
import tkinter as tk
# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Set the title of the window


# Load the icon file
icon = tk.PhotoImage(file="ant.gif")  # Replace 'icon_path.gif' with your icon file

# Set the icon for the window
root.iconphoto(True, icon)



# Set the icon for the turtle window


url = "https://discord.com/channels/1175458143988351049/1175458143988351052"

gameplay = "start"
wn_x,wn_y = pyautogui.size()

original_image = Image.open("wall_top.gif")

rotated = original_image.rotate(180)


rotated.save("walltop.gif")

image = Image.open("start screen.gif")

rotate = image.resize((wn_x,wn_y))


rotate.save("start.gif")



wn = turtle.Screen()
wn.bgcolor("green")
wn.tracer(0, 0)  # Adjust the tracer value
wn.title("ants raid")

wn.setup(wn_x,wn_y)




walle = False
discord = "joindiscord.gif"
iventory = "inventory.gif"
start_button = "play.gif"
rot = "rotated.gif"
block = "block.gif"
wood = "wood.gif"
ant = "ant.gif"
wasp = "wasp.gif"
walltop = "walltop.gif"
start = "start.gif"
walley = "wall.gif"
wall_top = "wall_top.gif"
wn.register_shape(block)
wn.register_shape(discord)
wn.register_shape(wall_top)
wn.register_shape(walltop)
wn.register_shape(wood)
wn.register_shape(ant)
wn.register_shape(iventory)
wn.register_shape(start)
wn.register_shape(start_button)
wn.register_shape(wasp)
wn.register_shape(rot)
wn.register_shape(walley)

class playbutton(turtle.Turtle):
  def __init__(self):
   turtle.Turtle.__init__(self)
   self.shape(start_button)
   self.pu()
   self.goto(0,0)
   self.showturtle()
class discordbutton(turtle.Turtle):
  def __init__(self,x,y):
   turtle.Turtle.__init__(self)
   self.shape(discord)
   self.pu()
   self.goto(x,y)
   self.showturtle()
class inventory(turtle.Turtle):
  def __init__(self,shape,x,y):
   turtle.Turtle.__init__(self)
   self.shape(shape)
   self.pu()
   self.goto(x,y)
   self.showturtle()
class start_screen(turtle.Turtle):
  def __init__(self):
   turtle.Turtle.__init__(self)
   self.shape(start)
   self.pu()
   self.goto(0,0)
   self.showturtle()

pen = turtle.Turtle()
pen.hideturtle()
class Ant_body(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.shape(ant)
        self.pu()
        self.goto(x, y)
        self.speed(10)
        self.height = 40
        self.width = 40
   

    def move(self,move):
        self.fd(move)  
class Wasp_body(turtle.Turtle):
    def __init__(self,x, y):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.shape(wasp)
        self.pu()
        self.goto(x, y)

    def move(self,move):
        self.backward(move)  # Modify the movement as needed

class castle_brick(turtle.Turtle):
  def __init__(self,shape,x,y):
   turtle.Turtle.__init__(self)
   self.shape(shape)
   self.pu()
   self.goto(x,y)
   self.height = 40
   self.width = 40
class Wall(turtle.Turtle):
  def __init__(self,shape):
   turtle.Turtle.__init__(self)
   self.shape(shape)
   self.pu()
   self.goto(0,0)
   self.hideturtle()
   self.height = 40
   self.width = 40
walls = []

wall = Wall(wood)

l = inventory(iventory,0,-wn_y/2 + 120)
ants = []
for i in range(20):
    ants.append(Ant_body(-wn_x + 40 * 30, random.randint((-wn_y / 2) + 40 * 4, (wn_y / 2) - 40 * 4)))
wasps = []
for i in range(20):
    wasps.append(Wasp_body(wn_x - 40 * 30, random.randint((-wn_y / 2) + 40 * 4, (wn_y / 2) - 40 * 4)))
castles = []
for i in range(int(wn_y)):
   castles.append(castle_brick(walley, -wn_x / 2 + 20, -wn_y + ((i+1) * 40)))
castles2 = []
for i in range(int(wn_y)):
   castles2.append(castle_brick(walley, -wn_x / 2 + 40, -wn_y + ((i+1) * 40)))
castlestop2 = []
for i in range(int(wn_y)):
   castlestop2.append(castle_brick(wall_top, -wn_x / 2 + 80, -wn_y + ((i+1) * 80)))
castlesl = []
for i in range(int(wn_y)):
   castlesl.append(castle_brick(walley, wn_x / 2 - 20, wn_y - ((i+1) * 40)))
castlesl2 = []
for i in range(int(wn_y)):
   castlesl2.append(castle_brick(walley, wn_x / 2 - 40, wn_y - ((i+1) * 40)))
castlestopl2 = []
for i in range(int(wn_y)):
   castlestopl2.append(castle_brick(walltop, wn_x / 2 - 80, wn_y - ((i+1) * 80)))






start = start_screen()
play = playbutton()
disc = discordbutton(-wn_x/2 + 160,-wn_y/2 + 260)

def onclick(x, y):
    global gameplay
    if gameplay == "start":
        if start.distance(x, y) < 40:  # Assuming the distance is less than 40 for the button
            gameplay = "game"
            print("done")
        elif disc.distance(x, y) < 150:  # Assuming the distance is less than 20 for the button
            webbrowser.open(url)
            print("Discord button clicked")
    elif gameplay == "game":
        wall.goto(x, y)
        wall.showturtle()
        wall.stamp()
        walls.append((x, y))

        
wn.listen()
wn.onclick(onclick)

running = True

while running:
    if gameplay == "game":
     play.hideturtle()
     start.hideturtle()
     disc.ht()
     for ant in ants:
       ant.move(random.randint(1,3))
       for wall_pos in walls:
           if ant.distance(wall_pos) < 40:
               ant.hideturtle()
               print("collision")
     
    else:
       play.showturtle()
       start.showturtle()
       disc.showturtle()
    
    pen.clear()
    pen.write("hi")
    wn.update()