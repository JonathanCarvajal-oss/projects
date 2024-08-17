#Balas
import pygame
class Balas: #definir un clase
    def __init__(self, x, y): #funcion de inicializacion
       self.x = x #EJE X
       self.y = y #EJE Y
       self.ancho = 20
       self.alto = 20
       self.velocidad = 10 #SEGUNDOS
       self.color = "#ffffff" #blanco
       self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #rectangulo
       
    #Dibujar el rectangulo 
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)
    
    def movimiento(self):
        self.y -= self.velocidad