equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−",
}


def morse_a_caracter_plano(caracter):
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        return ""

def codigo_morse(TEXTO_PLANO):
    TEXTO_PLANO = TEXTO_PLANO.upper()
    morse = ""
    for caracter in TEXTO_PLANO:
        caracter_codificado = morse_a_caracter_plano(morse)
        a = morse + caracter_codificado + " "
    return a

palabra = input('Digite un apalabra: ')
print('codificado:')
codificado = codigo_morse(palabra)

#echo por luis
#mensaje = input('Ingrese el mesaje que desea: ')
#traduce = ''

#traduce mas mosrse_code en rango de char
#for char in mensaje:
#    traduce =+ morse_code[char] + " "
    
#print(traduce)