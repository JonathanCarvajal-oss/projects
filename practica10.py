def sumar(lista):
    suma = 0
    for numero in lista:
        if numero %2 == 0: #solo suma los pares 
            suma += numero
        else:
            suma += numero #le agrege para que sumara todos 
    return suma

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'La suma de las lista {numero} es:', sumar(numero))

#n % 2 = 0 es par (numeros pares)
#n % 2 = 1 es impar (numeros impares)

#solucion del  porfe
#solo quito el if y movio suma al for

#Practica 11
#funcion LAMBDA (es para operacines sencillas en pocas lineas)
suma = lambda a,b: a+b
print(suma(2,3))

numeros = [1,2,3,4,5,6,7]
pares = list(filter(lambda x : x%2 == 0, numeros)) #filtra todos los numero pares de la lista (x%2 == 1 impar)
print(pares)

#LIST = convertir u ntipo a lista 
#FILTER = filtra recibiendo una funcion y un parametro

#Practica 12
#suma todos los numero de un alista con errores en el codigo
numero1 = [4,-1,2,5,7,10,9,7]
total = 0

for i in range (len(numero1)-1): #-1 no va con range
    total = numero1[0] #no esta sumando, agarro el rango de la lista 0 es i
print(total)

#Atajos de teclaso 
# mover linea ALT + flechas arriba/abajo
# duplicar un alinea ALT +SHIFT + flechas
# borrar una linea (palaba o texto) CTRL + delete
# borrar linea entera CTRL + SHIFT + K
# seleccionar linea entera CTRL + L
# seleccionar palabra/frace en tod el archivo y cambairlo CTRL + SHIFT L 
# comentar o descomentar CTRL + cevilla C con piquito/ CTRL + K -> CTRL + C 
# crear archivo CTRL +N
# guardar CTRL + S 
# borrar CTRL + W 