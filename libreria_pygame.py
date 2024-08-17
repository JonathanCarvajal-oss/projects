#juego con la libreria pygame
import pygame
from personaje import Cubo
from enemigo import Enemigo
import random
from balas import Balas
pygame.init() #si no se ejecuta esto el tema de las fuentes no funcionan

#crear la pantalla del juego, que se pueda cerrar y manipular (constantes)
ANCHO = 1000
ALTO = 700 #pixeles
ventana = pygame.display.set_mode([ANCHO,ALTO]) #DISPLAY todo lo que teiene que ver con la pantalla 
FPS = 60
#fuentes del texto
fuente = pygame.font.SysFont('Doble', 40) #tipo de fuente y tamaño en pixele

#variables de diseño
jugando = True #mientras se juega sera verdadero
cubo=Cubo(ANCHO/2,ALTO-75) #esquina superior izquierda
enemigos = []
reloj = pygame.time.Clock()
#Tiempo milisegundos que pasa entre enimgos
tiempo_pasado= 0
tiempo_entre_emnemigos = 500
enemigos.append(Enemigo(ANCHO/2,100))
#sistema de vidas
vidas = 5 #vidas del cubo
puntos = 0

balas = []
ultima_bala = 0
tiempo_entre_balas = 200
def crear_bala():
    global ultima_bala
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas: #tiks que an pasado desde el inicio del juego
        balas.append(Balas(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()

def gestionar_teclas(teclas):
    if teclas[pygame.K_UP]: #hacia arriba
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_DOWN]: #hacia abajo
        cubo.y += cubo.velocidad
    if teclas[pygame.K_LEFT]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_RIGHT]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_SPACE]:
        #crear la bala 
        crear_bala()
        
while jugando and vidas > 0:
    eventos = pygame.event.get() #lista de cada evento que hay
    #devuelve un alsiat con todas la teclas pulsadas en el momento
    teclas = pygame.key.get_pressed()
    texto_vida = fuente.render(f'Vida: {vidas}', True,'#58d68d') #verde, imprmir el texto
    texto_puntos= fuente.render(f'Puntos: {puntos}', True,'#58d68d') #verde, imprmir el texto

    tiempo_pasado += reloj.tick(FPS)
    if tiempo_pasado > tiempo_entre_emnemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100)) #nuevo enemigo cada cierto tiempo
        tiempo_pasado = 0 #recetea a 0
    
    gestionar_teclas(teclas)
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    ventana.fill('Black')
    cubo.dibujar(ventana)
    
    for enemigo in enemigos:
        enemigo.dibujar(ventana)
        enemigo.movimiento()
        #Coliciones
        if pygame.Rect.colliderect(cubo.rect,enemigo.rect):
            vidas -= 1
            print(f'Te quedan {vidas} vidas!')
            enemigos.remove(enemigo)
        if enemigo.y > ALTO:
            
            enemigos.remove(enemigo) #elimina alos enemigos
        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1
                balas.remove(bala)
                puntos += 1
                
        if enemigo.vida <= 0:
            enemigos.remove(enemigo)
            
    for bala in balas:
        bala.dibujar(ventana)
        bala.movimiento()
    
    ventana.blit(texto_vida, (20,20)) #toma un objeto y lo pega, cordenadas donde se pega 
    ventana.blit(texto_puntos, (20,50)) #toma un objeto y lo pega, cordenadas donde se pega 

    pygame.display.update()   
quit()
