import turtle
import random

# List of names
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']

# Pick a random name
random_name = random.choice(names)

# Display it using Turtle
t = turtle.Turtle()
t.hideturtle()
t.write(f"Generated Name:\n{random_name}", align="center", font=("Arial", 24, "bold"))

turtle.done()   