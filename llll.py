def cortar_y_guardar_palabras(texto, inicio, fin, nombre_archivo):
    # Cortar el texto desde el índice de inicio hasta el índice de fin
    texto_cortado = texto[inicio:fin]

    # Dividir el texto cortado en palabras
    palabras = texto_cortado.split()

    # Abrir (o crear) el archivo y escribir las palabras en él
    with open(nombre_archivo, 'w') as archivo:
        for palabra in palabras:
            archivo.write(palabra + '\n')

# Solicitar entrada al usuario
texto = input("Introduce el texto: ")
inicio = int(input("Introduce el índice de inicio (número entero): "))
fin = int(input("Introduce el índice de fin (número entero): "))
nombre_archivo = "palabras_cortadas.txt"

# Verificar que los índices son válidos
if 0 <= inicio < fin <= len(texto):
    cortar_y_guardar_palabras(texto, inicio, fin, nombre_archivo)
    print(f"Las palabras cortadas se han guardado en '{nombre_archivo}'.")
else:
    print("Índices no válidos. Asegúrate de que el índice de inicio es menor que el índice de fin y ambos están dentro del rango del texto.")
