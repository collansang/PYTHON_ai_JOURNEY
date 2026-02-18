import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

t = turtle.Turtle()
t.speed(10)
t.width(2)
t.hideturtle()

n = 360

for i in range(n):
    color = colorsys.hsv_to_rgb(i/n, 1, 1)
    t.pencolor(color)
    t.forward(i +0.8)
    t.right(59)
    
turtle.done()

