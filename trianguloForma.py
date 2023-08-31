from turtle import *
#tri = turtle.Turtle()   ## Variable que usará las funciones de la biblioteca Turtle
setup(600,500)   ## Tamaño de la ventana - setup(ancho, alto, posicionX, posicionY
title ("Triangulo recursivo")
bgcolor("black")
## Configuración inicial
speed(8)  # Velocidad de dibujo (1 = lento, 10 = rápido)

# Primer triángulo espejo
hideturtle() 
#left(120)
goto(0,0)
fillcolor("#a76394")
begin_fill()
for _ in range(3):
    right(240)
    forward(190)
end_fill()

# Segundo triángulo interior espejo
penup()
goto(-15,10)
left(360)
pendown()
fillcolor("#904d7e")
begin_fill()
for _ in range (3):
    right(240)
    forward(160)
end_fill()

# Tercer triángulo interior espejo
penup()
goto(-30,20)
pendown()
fillcolor("#783668")
begin_fill()
for _ in range (3):
    right(240)
    forward(130)
end_fill()

# Cuarto triángulo interior espejo
penup()
goto(-45,32)
pendown()
fillcolor("#612052")
begin_fill()
for _ in range (3):
    right(240)
    forward(100)
end_fill()

# Quinto triángulo interior espejo
penup()
goto(-60,40)
pendown()
fillcolor("#49093c")
begin_fill()
for _ in range (3):
    right(240)
    forward(70)
end_fill()

# Cierra la ventana al hacer clic
exitonclick()