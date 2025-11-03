archivo = open("./Archivos/texto2.txt", "r", encoding="utf-8")

'''
archivo.readline()
archivo.readline()
archivo.read(11)
datos = archivo.readline() ---> para buscar una palabra por numero de caracteres
archivo.close()
print(datos)
'''
archivo.seek(10) # solo para valores positivos
datos = archivo.readline()
archivo.close()
print(datos)












