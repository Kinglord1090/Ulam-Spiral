import colorsys
import random
import turtle


keshar = turtle.Turtle()
value = 1
color = 0.5
flag = False
shapes = ["circle", "square", "triangle", "turtle", "classic"]


turtle.delay(0)
turtle.bgcolor("black")
keshar.speed(0)
keshar.pensize(1)
keshar.turtlesize(1)
keshar.hideturtle()
keshar.fillcolor("white")
keshar.shape(shapes[random.randrange(len(shapes))])
#turtle.tracer(0, 0)


def isPrime(value, color, lower_lim, upper_lim):
	flag = False
	for x in range(2, value):
		if x <= int(value / 2):
			if value % x == 0:
				flag = True
				break
		else:
			break
	if flag != True:
		keshar.color(colorsys.hsv_to_rgb(color, 1, 1))
		keshar.stamp()
		color += random.randrange(lower_lim, upper_lim) / 1000
	return color

def shapeSquare(value, color, flag):
	for i in range(1, 51):
		for j in range(i):
			keshar.color("white")
			keshar.forward(10)
			value += 1
			color = isPrime(value, color, 5, 21)
		keshar.left(90)

def shapeCircle(value, color, flag):
	for i in range(300):
		value += 1
		keshar.forward(i / 5)
		keshar.left(5)
		color = isPrime(value, color, 20, 41)
		keshar.left(5)

if random.randrange(2) == 0:
	shapeSquare(value, color, flag)
	if random.randrange(2) == 0:
		keshar.penup()
else:
	shapeCircle(value, color, flag)

#turtle.update()
turtle.done()
