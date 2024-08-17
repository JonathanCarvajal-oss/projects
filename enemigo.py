import pygame

class Enemigo: #definir un clase
    def __init__(self, x, y): #funcion de inicializacion
       self.x = x #EJE X
       self.y = y #EJE Y
       self.ancho = 50
       self.alto = 50
       self.velocidad = 5 #SEGUNDOS
       self.color = "#ea1c1c" #ROJO
       self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #rectangulo
       self.vida = 3
       
    #Dibujar el rectangulo 
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)
    
    def movimiento(self):
        self.y += self.velocidad