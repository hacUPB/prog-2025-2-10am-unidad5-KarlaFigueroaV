import csv

with open('C:\\Users\\B09S202est\\Documents\\Programación-2025\\prog-2025-2-10am-unidad5-KarlaFigueroaV\\Archivos\\Variables.csv', 'r') as csvfile:
    lector = csv.reader(csvfile, delimiter=";")  # se utilza el método reader
    print(lector) 
    encabezado = next(lector) # salta la primera linea (no imprime los textos)
     # print(encabezado)
    presion = []
    print(encabezado[3]) 
    for fila in lector:    # Con el for se itera sobre el objeto
        fila[3] = fila[3].replace(',','.')
        dato = float(fila[3]) #fila es una lista
        presion.append(dato)

print(presion)