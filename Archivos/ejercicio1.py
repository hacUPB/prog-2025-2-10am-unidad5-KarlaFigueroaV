# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = "Ejercicio.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"

# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(ubicacion+"\\"+nombre_archivo, "w", encoding="utf-8") as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = int(input("Ingrese los datos que desea escribir en el archivo: "))
    numeros = float(input("Ingrese un número: "))
    archivo.write(datos)
    archivo.write(numeros)


# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)