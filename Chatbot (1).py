usuario =input('Bienvenido/a mi nombre es ATHENEA y soy un ChatBot creado por Steven Salas y puedo hacer varias cosasas (Operaciones Basicas, Jugar, hablar de algun tema que sea de su interes) \nLe voy a mostrar un menu de las opciones disponibles y usted me digita el numero de la operacion que desea realizar \n1- Operaciones basicas: \n2- Jugar: \n3- Hablar: \n ')

#Operaciones basicas
if usuario == "1":
  
  print('Usted a escogido las operaciones basicas le voy a presentar las opciones que tiene disponibles')
  usuario= int(input("Digite la opcion que desea realizar. \n1 Suma: \n2 Resta: \n3 Multplicacion: \n4 Divison: \n5 Salir: " ))
  if usuario == 1:
    n1=int(input('Digite el primer numero que desea sumar: '))
    n2=int(input('Digite el segundo numero que desea sumar: '))
    re=n1+n2
    print('El resulatado de la suma es', re)
  if usuario == 2:
    n1=int(input('Digite el primer numero que desea restar: ' ))
    n2=int(input('Digite el segundo numero que desea restar: ' ))
    re=n1-n2
    print('El resultado de la de la resta es', re )
  if usuario == 3:
    n1 = int(input('Digite el primer numero que desea multiplicar: ' ))
    n2 = int(input('Digite el segundo numero que desea multiplicar: ' ))
    re = n1 * n2
    print('El resultado de la de la multiplicacion es', re )
  if usuario == 4:
    try:
        n1 = int(input('Digite el primer número que desea dividir: '))
        n2 = int(input('Digite el segundo número que desea dividir: '))
        re = n1 / n2  
        print('El resultado de la división es:', re)
    except ZeroDivisionError:
        print('Error: No se puede dividir por cero.')
  if usuario == 5:
    print("Gracias por usar la calculadora")

#Juegos
import random #libreria random
import time #libreria time
import os #libreria sistema operatvo

if usuario == "Juego" or "juego":
  print ('Usted escogio juegos')
  opciones=int(input("Le voy a mostrar las opciones de juego que tiene \n1- Memoria \n2- Ahorcado \n3- Piedra Papel o Tijera \n"))
  if opciones == 1: 
    print('Usted escogio el juego de memorjuegoia')
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