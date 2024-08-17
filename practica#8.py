#Video#8 indexacion y recortes 
nom = input('Digite su nombre completo: ')
#print(primer_nom[1]) --> imprimira una letra de la cadena
primer_nom = nom[0:8] #toma todo lo que le indiques(recordar siempre dejar 1 más)
print('Hola ' + primer_nom + ' un gusto en conocerte')

apellidos = nom[9:] #Toma del aracter 9 a todo el resto
print('Tus apellidos son: ' + apellidos + ' Correcto?')

nombre_dos = nom[0:9:2] #el dos es para tomar cada dos caracteres
nombre_dos = nom[::2] #Toma todo la cadena de dos en dos
nombre_invertido = nom [::-1] #devuelve la cadena ivertida
print(nombre_dos)
print(nombre_invertido)

#recortes en cadenas (acostumbrarse a usarlo)
website = "http://www.google.com"
slice = slice(11,-4) #Objeto de corte (el 11 donde comienza, el -4 donde comienza en negativo) funcion slice
print(website[slice])

#otra forma de imprimir mas facíl
#sitio = website[slice]
#print(sitio)
