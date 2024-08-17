import pygame

class Cubo: #definir un clase
    def __init__(self, x, y): #funcion de inicializacion
       self.x = x
       self.y = y
       self.ancho = 30
       self.alto = 30
       self.velocidad = 10
       self.color = "#2980b9" #azul 
       self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #rectangulo
       
    #Dibujar el rectangulo 
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)