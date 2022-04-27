import turtle
t=turtle Turtle()
s=trutle.Screen()

s.bgcolor('black')
tiwidth(2)
t.speed(15)
col=("yellow","green","red","white")

for i in range(300):
  t.pencolor(col[i%4])
  t.forward(i*4)
  t.right(137
