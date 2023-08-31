from turtle import *

setup(800,700) 
title ("Circulo")
bgcolor ("#49093c")
color("white")
hideturtle() 
r = 50   #declaramos la radio del circulo
#circle(r)

for i in range(7):
    circle(r * i)
    up()
    sety((r * i)*(-1)) #Establece la segunda coordenada de la tortuga a y, deja la primera coordenada sin cambios.
    down()

exitonclick()