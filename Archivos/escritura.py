ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
# \ se usa para comandos de texto
nombre_archivo = "frutas2.txt"
modo = "x"
fp = open(ubicacion+"\\"+nombre_archivo, modo)
frase = input("Por favor ingresa una frase: ")
# solicitar una variable entera y una float al usuario y la escriben en el archivo
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
# La escriben en el archivo
fp.write(frase + "\n" )
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura) + "\n")
fp.close()
