nombre_archivo = "canciones.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
with open(ubicacion+"\\"+nombre_archivo, "r", encoding="utf-8") as archivo:
    # Leer todas las líneas dento de una lista
    lista = archivo.readlines()

# se imprime la lista elemento por elemento
for c in lista:
    print(c)