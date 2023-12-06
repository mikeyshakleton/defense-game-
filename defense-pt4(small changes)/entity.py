import turtle

class playbutton(turtle.Turtle):
  def __init__(self,shape):
   turtle.Turtle.__init__(self,shape)
   self.shape(shape)
   self.pu()
   self.goto(0,0)
   self.showturtle()
class discordbutton(turtle.Turtle):
  def __init__(self,shape,x,y):
   turtle.Turtle.__init__(self,shape)
   self.shape(shape)
   self.pu()
   self.goto(x,y)
   self.showturtle()
class inventory(turtle.Turtle):
  def __init__(self,shape,x,y):
   turtle.Turtle.__init__(self,shape)
   self.shape(shape)
   self.pu()
   self.goto(x,y)
   self.showturtle()
class start_screen(turtle.Turtle):
  def __init__(self,shape):
   turtle.Turtle.__init__(self,shape)
   self.shape(shape)
   self.pu()
   self.goto(0,0)
   self.showturtle()

pen = turtle.Turtle()
pen.hideturtle()
class Ant_body(turtle.Turtle):
    def __init__(self,shape,x,y):
        turtle.Turtle.__init__(self,shape)
        self.x = x
        self.y = y
        self.shape(shape)
        self.pu()
        self.goto(x, y)
        self.speed(10)
        self.height = 40
        self.width = 40
   

    def move(self,move):
        self.fd(move)  
class Wasp_body(turtle.Turtle):
    def __init__(self,shape,x, y):
        turtle.Turtle.__init__(self,shape)
        self.x = x
        self.y = y
        self.shape(shape)
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
