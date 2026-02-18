import turtle

t = turtle.Turtle()
t.speed(0)
colors = ['red', 'orange', 'yellow', 'green', 'blue']

for i in range(100):
    t.color(colors[i % 5])
    for _ in range(3):
        t.forward(50 + i * 2)
        t.right(120)
    t.right(30)

turtle.done()   