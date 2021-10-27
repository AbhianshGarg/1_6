#   a116_ladybug.py
import turtle as trtl


# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

#ladybug.speed(0)

heading_one = 90
heading_two = 270
ladybug.pensize(7)
while True:
  for i in range(3):
    ladybug.penup()
    ladybug.goto(0, -35)
    ladybug.pendown()
    ladybug.setheading(heading_one)
    ladybug.circle(50, 180)
    heading_one += 40
  for i in range(4):
    ladybug.penup()
    ladybug.goto(0, -35)
    ladybug.pendown()
    ladybug.setheading(heading_two)
    ladybug.circle(60, 180)
    heading_two -= 40
  break

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.setheading(0)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.color("black")


# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  xpos += 10
  ypos += 20
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots += 1
  # position next dots
  xpos = ypos + 25
  xpos = xpos + 15
  num_dot = num_dots + 1






ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()