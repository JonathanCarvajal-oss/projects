#operadores logicos and, or, not,etc -> nos permiyen hacer expreciones mas completas

edad = 20
nombre= 'Luis'

if edad == 20 and nombre == 'Lui':
     print(False)
if edad >= 18 and nombre == 'Luis':
    print(True)

#and -> Ambas tiene wque ser correctas 
#true and true = true
#false and true = false
#true and false = false
#false and false = false

#or -> Una sola tiene que ser correcta 
#true and true = true
#false and true = true
#true and false = true
#false and false = false

#Not
#not false = true
#not true = false