#  a116_buggy_image.py
import turtle as trtl

painter = trtl.Turtle()

#create body
painter.pensize(40)
painter.circle(20)

#number of legs
number_of_lines = 8
#length of legs
length_of_line = 70
#degree measure between each legs
degrees = 360 / number_of_lines
painter.pensize(5)
#creating legs
for n in range(number_of_lines):
  painter.goto(0,20)
  painter.setheading(degrees*n)
  painter.forward(length_of_line)
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()