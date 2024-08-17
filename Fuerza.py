#Forzar que el usuario introduzca un numero

num = input('Introdusca un numero: ')

while not num.isdigit(): #True si es numero falce si no es, while 'mientras'
    num = input('Vuelve a introdusca un numero: ')
print('Terminaste!')
