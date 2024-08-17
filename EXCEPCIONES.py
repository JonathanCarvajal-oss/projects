#Tratar con excepciones

#divicion por cero 
#print('Divición')
#num = int(input('Ingrese u nnumero: '))
#num2 = int(input('Ingrese u nnumero: '))

#try: 
#    print(num / num2)
#except ZeroDivisionError:
#    print('Error divicion por 0')

#Otro tipo de error
num = 1
num2 = 1

try:
    print('1' + 1)
except ZeroDivisionError:
    print('Division por 0')
except:
    print('Otro tipo de error')
