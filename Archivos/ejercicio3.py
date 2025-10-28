ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
nombre_archivo = "salida.csv"
modo = "w"
import csv
Nombre = ["Karla", "Andrea", "Mariana", "Isabella"]
Edad = [1,2,3,4]
Ciudad = ["Sincelejo", "Barranquilla", "Cartagena", "Medellín" ]

with open(ubicacion+"\\"+nombre_archivo, modo, newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(Nombre)
    escritor.writerow(Edad)
    escritor.writerow(Ciudad)
    
    lector = csv.reader(csvfile, delimiter=",")  
    print(lector) 
    presion = []
    for fila in lector:    # Con el for se itera sobre el objeto
        Edad = fila[1]
        Ciudad = fila[2]
        Nombre = fila[0]
