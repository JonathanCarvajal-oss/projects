
print("Bienvenido a la calculadora Seleccione la operacion que desea hacer")
print("Seleccione la operacion que desea realizae")
eleccion=int(input("Digite la opcion que desea realizar: 1 Si es suma,2 Si es una resta, 3 Si es una division, 4 Si es multiplicacion: "  ))

if eleccion==1:
    num1=int(input("Digite el numero que desea sumar"))
    num2=int(input("Digite el numero que desa sumar"))
    resultado= num1 + num2 
    print('El resultado es ',resultado)
if eleccion == 2:
    num3= int(input("Digite el numero que desea restar"))
    num4=int(input("Digite el numero que desea restar"))
    resultado1 = num3 - num4
    print('El resultado es',resultado1)
if eleccion==3:
    num5= int(input("Digite el numero que desea Dividir"))
    num6=int(input("Digite el numero que desea Dividir"))
    resultado2 = num5 / num6
    print('El resultado es',resultado2)
if eleccion == 4:
    num7=int(input("Digite el numero que desea multiplicar"))
    num8=int(input("Digite el numero que desee multiplicar"))
    resultado3 = num7 * num8
    print('El resultado es',resultado3)
