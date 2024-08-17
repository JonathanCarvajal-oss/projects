from turtle import *
from math import *


speed(0) #velocidad del turtle
bgcolor('black')
goto(0,-40) #mueve turtle a la posisción

for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90) 
        circle(150-j*6,90), lt(90) #arco de 90 grados con radio decreciente
        circle(150-j*6,90), rt(180)
    circle(40,24)

color('black')
shape('circle')
shape.ize(0.5)

#cambia el color de relleno de los circulos
fillcolor('#ff1616')
golden_arg = 137.508
phi = golden_arg*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x,y)
    setheading(i*golden_arg)
    pendown(), stamp()
    
    #color('black) Cambia el color del contorno de los círculos pequeños
    #fillcolor('#ff1616) cambia el color de rrelleno de los circulos pequeños
    
def circulo(x,y):
    penup(), goto(x,y), pendown()
    color('black'), fillcolor('#ff1616')
    begin_fill(), circle(3), end_fill()
    
def dibujar_M(x, y):
    pos_m = [(x, y), (x, y+4), (x, y+8), (x, y+12), (x, y+16), 
             (x, y+50), (x, y+24), (x+3, y+21), (x+6, y+18), 
             (x+9, y+15), (x+12, y+12), (x+15, y+15), (x+18, y+18), 
             (x+21, y+21), (x+24, y+24), (x+24, y+20), (x+24, y+16), 
             (x+24, y+12), (x+24, y+8), (x+24, y+4), (x+24, y), ]
    
    for pos in pos_m:
        circulo(*pos)

def dibujar_A(x, y):
    pos_a = [(x, y), (x+2, y+4), (x+4, y+8), (x+6, y+12), 
             (x+8, y+16), (x+10, y+20), (x+12, y+24), (x+14, y+20), 
             (x+16, y+16), (x+18, y+12), (x+20, y+8), (x+22, y+4), 
             (x+24, y), (x+8, y+8), (x+12, y+8), (x+16, y+8), ]
    for pos in pos_a:
        circulo(*pos)

#cambia el color de los circiulos grandes
dibujar_M(-28, 4), dibujar_A(10, 4)
dibujar_M(-28, -30), dibujar_A(10, -30)
circulo(12, -10), circulo (34, -6)

hideturtle()
mainloop()
done()
