import random #libreria random
import time #libreria time
import os #libreria sistema operatvo

minimo = 1
maximo = 9

while True:
    numero = str(random.randint(minimo,maximo))
    print(f'Recuerda elnumero {numero} ...')
    
    time.sleep(1.10) #numer en segundos 
    os.system('cls') #caso de windows cls linux clear- limpiar la consola
    intento = input('Introduce el numero: ')
    
    if intento == numero:
        print('Numero acertdo!')
        minimo += 10
        maximo *= 10
        
    else: 
        print('Fallaste, el numero era', numero)
        break