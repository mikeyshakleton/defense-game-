import turtle
import pyautogui
import random
import time
import webbrowser
from PIL import Image
from entity import *
url = "https://discord.com/channels/1175458143988351049/1175458143988351052"
gameplay = "start"
wn_x,wn_y = pyautogui.size()
print(f"{wn_x}x{wn_y}")
original_image = Image.open("wall_top.gif")
rotated = original_image.rotate(180)
rotated.save("walltop.gif")
image = Image.open("start screen.gif")
rotate = image.resize((wn_x,wn_y))
rotate.save("start.gif")
wn = turtle.Screen()
wn.setup(wn_x,wn_y)
wn.title("ants raid")
wn.bgcolor("green")
wn._root.overrideredirect(1)
wn.tracer(0, 0)
wn.title("ants raid")
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
char = [wall_top,walley,start,walltop,wasp,ant,wood,block,rot,start_button,iventory,discord]
for c in char:
   wn.register_shape(c)
walls = []
wall = Wall(wood)
l = inventory(iventory,0,-wn_y/2 + 120)
ants = []
for i in range(20):
    ants.append(Ant_body(ant,int(-wn_x + 40 * 30), random.randint(int((-wn_y / 2) + 40 * 4), int((wn_y / 2) - 40 * 4))))
wasps = []
for i in range(20):
    wasps.append(Wasp_body(wasp,int(wn_x - 40 * 30), random.randint(int((-wn_y / 2) + 40 * 4), int((wn_y / 2) - 40 * 4))))
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
start = start_screen(start)
play = playbutton(start_button)
disc = discordbutton(discord,-wn_x/2 + 160,-wn_y/2 + 260)
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
            ant.move(random.randint(1, 3))
            for wall_pos in walls:
                if ant.distance(wall_pos) < 40:
                    ant.hideturtle()
                    print("collision")
    else:
        play.showturtle()
        start.showturtle()
        disc.showturtle()

    # Draw or update elements here
    pen.clear()
    pen.write("hi")

    wn.update()  # Update the window

    print(f"{wn_x}x{wn_y}")  # Ensure this doesn't cause any issues

