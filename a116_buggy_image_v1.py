#  a116_buggy_image.py
import turtle as trtl

painter = trtl.Turtle()

painter.pensize(40)
painter.circle(20)

number_of_lines = 6
length_of_line = 70
degrees = 380 / number_of_lines
painter.pensize(5)

for n in range(number_of_lines):
  painter.goto(0,0)
  painter.setheading(degrees*n)
  painter.forward(length_of_line)
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()