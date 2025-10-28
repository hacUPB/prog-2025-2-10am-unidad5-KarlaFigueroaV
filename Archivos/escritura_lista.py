lista =["Luna nueva", "Decimas", "Imágenes", "Korazong", "Personas"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
modo = "x"
nombre_archivo = "canciones.txt"
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
for i in lista:
    fp.write(i + "\n")
fp.close()