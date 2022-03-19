from turtle import* 



#Small square
x1 = 200
forward(100)
left(90)
forward(x1)

left(90)
forward(x1)

left(90)
forward(x1)

left(90)
forward(x1)



#Bigger square
x = 275
y = 270
right(45)
penup()
forward(50)
left(135)
pendown()
forward(x)

left(90)
forward(y)
left(90)
forward(x)
left(90)
forward(y)

#bolding
forward(1)
left(90)
forward(x+1)
left(90)
forward(y+2)
left(90)
forward(x+2)
left(90)
forward(y+2)

forward(1)
left(90)
forward(x+1)
left(90)
forward(y+2)
left(90)
forward(x+2)
left(90)
forward(y+2)

forward(1)
left(90)
forward(x+1)
left(90)
forward(y+2)
left(90)
forward(x+2)
left(90)
forward(y+2)

forward(1)
left(90)
forward(x+1)
left(90)
forward(y+2)
left(90)
forward(x+2)
left(90)
forward(y+2)

#return to center
penup()
left(135)
forward(200)
right(45)


mainloop()