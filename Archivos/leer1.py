# Abrir el archivo y definir el modo
archivo = open("./Archivos/texto.txt", "r")
# Leer el archivo --> datos = archivo.read()
datos = archivo.readlines()
print(datos)
# cerrar el archivo
archivo.close()
# EOF constante que escribe cuando ha llegado al final del archivo
# for datos in archivo:  
    #print(datos[0]) --> Imprime la primera letra de cada linea
#archivo.readline es caracteres hasta donde se encuentre un enter
# Leer el archivo --> datos = archivo.read()
# datos = archivo.readlines() --> toma el texto y cada elemento de este como elementos de una lista 