#  a116_buggy_image.py
import turtle as trtl

painter = trtl.Turtle()

#create body
painter.pensize(40)
painter.circle(20)

#create body
d = -15
z = 25
painter.pensize(1)
for i in range(2):
  painter.penup()
  painter.goto(d, z)
  painter.pendown()
  painter.fillcolor('pink')
  painter.begin_fill()
  painter.circle(5)
  painter.end_fill()
  d += 10
  z += 8

#number of legs
number_of_lines = 8
#length of legs
length_of_line = 70
#degree measure between each legs
degrees = 180 / number_of_lines
painter.pensize(5)
#creating legs

for y in range(1):
  for n in range(4):
    painter.goto(0,20)
    painter.setheading(degrees*n)
    painter.forward(length_of_line)

  degrees = 240
  for x in range(0, 80, 20):
    painter.goto(0,20)
    painter.setheading(degrees - x)
    painter.forward(length_of_line)
  painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()