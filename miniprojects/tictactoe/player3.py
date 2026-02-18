import turtle

def draw_spiral():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    for i in range(36):
        for _ in range(4):
            my_turtle.forward(100)
            my_turtle.right(90)
        my_turtle.right(10)
    turtle.done()

draw_spiral()   