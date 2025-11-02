# Importamos los módulos necesarios
import os                      # Para trabajar con archivos y carpetas del sistema
import csv                     # Para leer archivos CSV
import matplotlib.pyplot as plt  # Para crear gráficos como barras y dispersión

# Función para mostrar archivos en una carpeta
def mostrar_archivos():
    print("\n1) Carpeta actual")
    print("2) Ingresar otra carpeta")
    opcion_usuario = input("Seleccione una opción: ").strip()

    if opcion_usuario != "2":
        ruta_carpeta = "."
    else:
        ruta_carpeta = input("Ingrese la ruta deseada: ").strip()

    try:
        ruta_absoluta = os.path.abspath(ruta_carpeta)
        print("\nElementos en la ruta:", ruta_absoluta)
        lista_elementos = os.listdir(ruta_carpeta)
        for elemento in lista_elementos:
            print(" •", elemento)
    except Exception as error:  # Se utilizo IA para no utilizar condicionales si no TRY 
        print("No se pudo acceder a la carpeta:", error)

# Función para leer el contenido de un archivo de texto
def leer_archivo_txt(ruta_archivo_txt):
    try:
        archivo = open(ruta_archivo_txt, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        return contenido
    except Exception as error:  # Se utilizo IA para no utilizar condicionales si no TRY 
        print("Error al intentar leer el archivo:", error)
        return None

# Función para escribir contenido en un archivo de texto
def escribir_archivo_txt(ruta_archivo_txt, contenido_txt):
    try:
        archivo = open(ruta_archivo_txt, "w", encoding="utf-8")
        archivo.write(contenido_txt)
        archivo.close()
        return True
    except Exception as error:              # Se utilizo IA para no utilizar condicionales si no TRY 
        print("No fue posible guardar el archivo:", error)
        return False

# Función para contar palabras y caracteres en un archivo de texto
def contar_txt(ruta_archivo_txt):
    contenido = leer_archivo_txt(ruta_archivo_txt)
    if contenido is None:
        return

    lista_palabras = contenido.split()
    cantidad_palabras = len(lista_palabras)
    cantidad_caracteres_con_espacios = len(contenido)

    cantidad_caracteres_sin_espacios = 0
    for caracter in contenido:
        if not caracter.isspace():
            cantidad_caracteres_sin_espacios += 1

    print("\nTotal de palabras:", cantidad_palabras)
    print("Caracteres (incluyen espacios):", cantidad_caracteres_con_espacios)
    print("Caracteres (sin espacios):", cantidad_caracteres_sin_espacios)

# Función para reemplazar texto en un archivo
def reemplazar_txt(ruta_archivo_txt):
    contenido = leer_archivo_txt(ruta_archivo_txt)
    if contenido is None:
        return

    texto_a_buscar = input("Texto a buscar: ").strip()
    texto_nuevo = input("Nuevo texto: ").strip()

    if texto_a_buscar == "":
        print("Debe ingresar una palabra válida.")
        return

    contenido_modificado = contenido.replace(texto_a_buscar, texto_nuevo)
    exito = escribir_archivo_txt(ruta_archivo_txt, contenido_modificado)

    if exito:
        print("El contenido fue actualizado correctamente.")

# Función para contar vocales y graficarlas
def graficar_vocales_txt(ruta_archivo_txt):
    contenido = leer_archivo_txt(ruta_archivo_txt)
    if contenido is None:
        return

    lista_vocales = ["a", "e", "i", "o", "u"]
    conteo_vocales = [0, 0, 0, 0, 0]

    contenido_minuscula = contenido.lower()
    for letra in contenido_minuscula:
        if letra in lista_vocales:
            posicion = lista_vocales.index(letra)
            conteo_vocales[posicion] += 1

    print("\nFrecuencia de vocales:")
    for i in range(5):
        print(lista_vocales[i], "→", conteo_vocales[i])

    plt.bar(lista_vocales, conteo_vocales, color="skyblue")
    plt.title("Conteo de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Cantidad")
    plt.show()

def submenu_txt():
    ruta_archivo_txt = input("Ruta del archivo de texto: ").strip()

    while True:
        print("\nOpciones TXT:")
        print("1) Contar")
        print("2) Reemplazar")
        print("3) Gráfico de vocales")
        print("4) Volver")

        opcion_txt = input("Elija una opción: ").strip()

        if opcion_txt == "1":
            contar_txt(ruta_archivo_txt)
        elif opcion_txt == "2":
            reemplazar_txt(ruta_archivo_txt)
        elif opcion_txt == "3":
            graficar_vocales_txt(ruta_archivo_txt)
        elif opcion_txt == "4":
            break
        else:
            print("Esa opción no es válida.")

# Intenta abrir un archivo CSV con diferentes codificaciones
def abrir_archivo_csv(ruta_archivo_csv):
    codificaciones = ["utf-8", "latin-1", "cp1252"]
    for codificacion in codificaciones:
        try:
            archivo = open(ruta_archivo_csv, "r", newline="", encoding=codificacion, errors="replace")
            lector = csv.reader(archivo, delimiter=";")
            return archivo, lector
        except Exception:
            continue      # Se utilizo IA para enteder la función del TRY
    print("No se pudo abrir el archivo con ninguna codificación compatible.")
    return None, None

# Muestra las primeras 15 filas del archivo CSV
def mostrar_encabezado_csv(ruta_archivo_csv):
    archivo, lector = abrir_archivo_csv(ruta_archivo_csv)
    if lector is None:
        return

    contador = 0
    try:
        for fila in lector:
            print(fila)
            contador += 1
            if contador >= 15:
                break
    finally:
        try:
            archivo.close()
        except:
            pass

# Lee todas las filas del archivo CSV y las guarda en una lista
def leer_todo_csv(ruta_archivo_csv):
    archivo, lector = abrir_archivo_csv(ruta_archivo_csv)
    if lector is None:
        return None

    lista_filas = []
    try:
        for fila in lector:
            lista_filas.append(fila)
    finally:
        try:
            archivo.close()
        except:
            pass
    return lista_filas

# Busca el índice de una columna por nombre o número
def obtener_indice_columna(encabezados, entrada_usuario):
    if entrada_usuario.isdigit():
        indice = int(entrada_usuario)
        if indice >= 0 and indice < len(encabezados):
            return indice
        else:
            return -1
    for i in range(len(encabezados)):
        if encabezados[i] == entrada_usuario:
            return i
    return -1

# Convierte los valores de una columna a números flotantes
def convertir_columna_a_float(lista_filas, indice_columna):
    lista_valores = []
    for fila in lista_filas:
        if indice_columna < len(fila):
            texto = fila[indice_columna].strip()
            if texto != "":
                try:
                    numero = float(texto.replace(",", "."))
                    lista_valores.append(numero)
                except:
                    pass
    return lista_valores

# Calcula estadísticas básicas de una lista de números
def calcular_estadisticas(lista_valores):
    cantidad = len(lista_valores)
    if cantidad == 0:
        return (0, None, None, None, None, None)

    suma = 0
    for valor in lista_valores:
        suma += valor
    promedio = suma / cantidad

    lista_ordenada = sorted(lista_valores)
    minimo = lista_ordenada[0]
    maximo = lista_ordenada[-1]

    if cantidad % 2 == 1:
        mediana = lista_ordenada[cantidad // 2]
    else:
        mediana = (lista_ordenada[cantidad // 2 - 1] + lista_ordenada[cantidad // 2]) / 2

    suma_cuadrados = 0
    for valor in lista_valores:
        diferencia = valor - promedio
        suma_cuadrados += diferencia ** 2
    desviacion = (suma_cuadrados / cantidad) ** 0.5

    return (cantidad, promedio, mediana, desviacion, minimo, maximo)

# Muestra estadísticas de una columna numérica del CSV
def mostrar_estadisticas_csv(ruta_archivo_csv):
    lista_filas = leer_todo_csv(ruta_archivo_csv)
    if not lista_filas:
        print("CSV vacío o no válido.")
        return

    encabezados = lista_filas[0]
    print("\nEncabezados:")
    for i in range(len(encabezados)):
        print("  [" + str(i) + "] " + encabezados[i])

    entrada_usuario = input("Nombre o índice de columna: ").strip()
    indice_columna = obtener_indice_columna(encabezados, entrada_usuario)
    if indice_columna == -1:
        print("Columna no encontrada.")
        return

    lista_valores = convertir_columna_a_float(lista_filas[1:], indice_columna)
    cantidad, promedio, mediana, desviacion, minimo, maximo = calcular_estadisticas(lista_valores)

    print("\nCantidad:", cantidad)
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)

# Grafica los valores de una columna numérica del CSV
def graficar_columna_csv(ruta_archivo_csv):
    lista_filas = leer_todo_csv(ruta_archivo_csv)
    if not lista_filas:
        print("CSV vacío o no válido.")
        return

    encabezados = lista_filas[0]
    print("\nEncabezados:")
    for i in range(len(encabezados)):
        print("  [" + str(i) + "] " + encabezados[i])

    entrada_usuario = input("Columna numérica (nombre o índice): ").strip()
    indice = obtener_indice_columna(encabezados, entrada_usuario)
    if indice == -1:
        print("Columna no encontrada.")
        return

    valores = convertir_columna_a_float(lista_filas[1:], indice)
    if not valores:
        print("No hay datos numéricos válidos.")
        return

    # Gráfico de dispersión
    xs = []
    ys = []
    for i in range(len(valores)):
        xs.append(i)
        ys.append(valores[i])

    plt.figure()
    plt.scatter(xs, ys)
    plt.title("Dispersión - " + encabezados[indice])
    plt.xlabel("Índice")
    plt.ylabel(encabezados[indice])
    plt.show()

    # Gráfico de barras por rangos
    minimo = min(valores)
    maximo = max(valores)
    bins = 5
    ancho = (maximo - minimo) / bins if bins > 0 else 1

    etiquetas = []
    for b in range(bins):
        li = minimo + b * ancho
        if b < bins - 1:
            ls = minimo + (b + 1) * ancho
        else:
            ls = maximo
        etiqueta = str(round(li, 2)) + "-" + str(round(ls, 2))
        etiquetas.append(etiqueta)

    frecuencias = []
    for _ in range(bins):
        frecuencias.append(0)

    for valor in valores:
        for b in range(bins):
            partes = etiquetas[b].split("-")
            li = float(partes[0])
            ls = float(partes[1])
            if (valor >= li and valor < ls) or (b == bins - 1 and valor <= ls):
                frecuencias[b] += 1
                break

    plt.figure()
    plt.bar(etiquetas, frecuencias, color="mediumseagreen")
    plt.title("Barras por rangos - " + encabezados[indice])
    plt.xlabel("Rango")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Menú para trabajar con archivos CSV
def submenu_csv():
    ruta_archivo_csv = input("Ruta del archivo CSV: ").strip()

    while True:
        print("\nOpciones CSV:")
        print("1) Ver primeras filas")
        print("2) Estadísticas")
        print("3) Graficar columna")
        print("4) Volver")

        opcion_csv = input("Seleccione una opción: ").strip()

        if opcion_csv == "1":
            mostrar_encabezado_csv(ruta_archivo_csv)
        elif opcion_csv == "2":
            mostrar_estadisticas_csv(ruta_archivo_csv)
        elif opcion_csv == "3":
            graficar_columna_csv(ruta_archivo_csv)
        elif opcion_csv == "4":
            break
        else:
            print("Opción no válida.")

# Menú principal del programa
def main():
    while True:
        print("\n--- Menú principal ---")
        print("1) Mostrar archivos")
        print("2) Procesar archivo TXT")
        print("3) Procesar archivo CSV")
        print("4) Salir")

        opcion_principal = input("Seleccione una opción: ").strip()

        if opcion_principal == "1":
            mostrar_archivos()
        elif opcion_principal == "2":
            submenu_txt()
        elif opcion_principal == "3":
            submenu_csv()
        elif opcion_principal == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

# Activación del programa
if __name__ == "__main__":
    main()
