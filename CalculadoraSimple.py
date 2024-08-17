print('D = División '
      ' M = Multiplicación' 
      ' R = Resta '
      ' S = Suma ')
letra = input('Letra: ')

i = float(input('numeros: ') )
O = float(input('2do numero: '))
result = ()

while True:

    if letra == 'D' or 'd':
        result = i / O
        continue

    elif letra == 'M' or 'm':
        result = i * O
        continue

    elif letra == 'S' or 's':
        result = i + O
        continue

    elif letra == 'R' or 'r':
        result = i - O
        continue
    
    print('Tu resultado es: ' + str(result))
    
    else: print ('Si quieres "salir" escribe "adios"')

if letra == "adios" or "Adios":
    print('nos vemos la proxima')
exit