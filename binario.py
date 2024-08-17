#convertir un numero decimal a binario 

def decimal_binario(decimal): #funcion del numero decimal
    if decimal == 0:
        return '0'
    binario = ''
    
    while decimal > 0:
        res = decimal % 2
        binario = str(res) + binario #imprimir el res y a la par binario
        decimal = decimal // 2
    return binario

print(decimal_binario(129)) 