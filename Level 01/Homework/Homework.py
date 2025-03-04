from turtle import *


#we want to paint a house
width(5)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)

right(90)
forward(60)

right(90)
forward(120)
end_fill()
#drawing roof
penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)

forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(20, 180)
pendown()

color("green")

left(30)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)


penup()
goto(180, 180)
pendown()

color("green")

left(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)


















exitonclick()