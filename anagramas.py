#Funcion que reciba dos cadenas de texto y devuelva si son anagrams entre si o no
#sorted() ordenar alfabeticamnete cadenas


def es_anagrama(usuario, usuario_dos):
    print('Soy un anagramista, digita tus anagrmsa.')
    usuario = input('Digite una palabra: \n')
    usuario_dos = input('Digite la segunda palbra: \n')
    
    if len(usuario) != len(usuario_dos):
        return False
    if sorted(usuario) == sorted(usuario_dos):
        print(f'Sus cadenas son anagrmas "{usuario, usuario_dos}.')
    else:
        return False
print(es_anagrama('usuario', 'usuario_dos'))


def es_anagrama(p1, p2):
    if len(p1) != len(p2):
        return False
    if sorted(p1) == sorted(p2):
        return True
    else:
        return False
print(es_anagrama('boca', 'cabo'))
print(es_anagrama('Hola', 'Mundo'))