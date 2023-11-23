import socket
import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Player Movement")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

# Player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("red")
player.penup()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5050))
server.listen()

print("Server is running...")

while True:
    client, address = server.accept()
    print(f"Connection from {address} has been established!")

    command = client.recv(1024).decode()
    if command == 'up':
        player.setheading(90)
        player.forward(10)
    elif command == 'down':
        player.setheading(270)
        player.forward(10)
    elif command == 'left':
        player.setheading(180)
        player.forward(10)
    elif command == 'right':
        player.setheading(0)
        player.forward(10)

    client.close()