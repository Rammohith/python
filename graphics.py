from turtle import *
import random
#moving forward

# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)





#drawing dashed line

# turtle = Turtle()
# turtle.shape("turtle")

# for i in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()





#printing all shapes 

colors=["lavender","orchid","deep pink","peach puff","crimson","black","orange","blue","grey"]

# turtle = Turtle()
# def draw_turtle(no_of_sides):
#     angle = 360 / no_of_sides
#     for i in range(no_of_sides):
#         turtle.forward(100)
#         turtle.right(angle)


# for i in range(3,11):
#     turtle.color(random.choice(colors))
#     draw_turtle(i)






# generating random walk
directions = [0, 90, 180, 270]
turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
for i in range(200):
    turtle.color(random.choice(colors))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()