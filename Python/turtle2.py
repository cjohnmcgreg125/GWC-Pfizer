import turtle
myTurtle = turtle.Turtle()
def draw_star(size,color):
    count = 0
    angle = 144
    while count <= 5:
        turtle.forward(size)
        turtle.right(angle)
        count += 1
    return
draw_star(100,"thistle")
turtle.bgcolor("lavender")
myTurtle.color("thistle")
turtle.done()
