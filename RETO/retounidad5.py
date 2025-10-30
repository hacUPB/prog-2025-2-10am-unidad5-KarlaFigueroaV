import os, sys, csv

TIENE_MATPLOTLIB = True
try:
    import matplotlib.pyplot as plt
except Exception:
    TIENE_MATPLOTLIB = False

# ---------- Utilidades ----------
def limpiar_pantalla():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass

def pausar():
    try:
        input("\nPresione Enter para continuar...")
    except:
        pass

def mostrar_archivos():
    print("\n1) Carpeta actual\n2) Ingresar otra carpeta")
    opcion = input("Seleccione una opción: ").strip()
    ruta = "." if opcion != "2" else input("Ingrese la ruta deseada: ").strip()
    try:
        print("\nElementos en la ruta:", os.path.abspath(ruta))
        for nombre_archivo in os.listdir(ruta):
            print(nombre_archivo)
    except Exception as error:
        print("No se pudo acceder a la carpeta:", error)

# ---------- TXT ----------
def leer_archivo_txt(ruta_txt):
    try:
        with open(ruta_txt, "r", encoding="utf-8") as archivo_txt:
            return archivo_txt.read()
    except Exception as error:
        print("Error al intentar leer el archivo:", error)
        return None

def escribir_archivo_txt(ruta_txt, contenido_txt):
    try:
        with open(ruta_txt, "w", encoding="utf-8") as archivo_txt:
            archivo_txt.write(contenido_txt)
            return True
    except Exception as error:
        print("No fue posible guardar el archivo:", error)
        return False

def contar_txt(ruta_txt):
    contenido = leer_archivo_txt(ruta_txt)
    if contenido is None:
        return
    palabras = contenido.split()
    cantidad_palabras = len(palabras)
    caracteres_con_espacios = len(contenido)
    caracteres_sin_espacios = sum(1 for caracter in contenido if not caracter.isspace())
    print("\nTotal de palabras:", cantidad_palabras)
    print("Caracteres (incluyen espacios):", caracteres_con_espacios)
    print("Caracteres (sin espacios):", caracteres_sin_espacios)

def reemplazar_txt(ruta_txt):
    contenido = leer_archivo_txt(ruta_txt)
    if contenido is None:
        return
    palabra_original = input("Texto a buscar: ").strip()
    palabra_nueva = input("Nuevo texto: ").strip()
    if palabra_original == "":
        print("Debe ingresar una palabra válida.")
        return
    if escribir_archivo_txt(ruta_txt, contenido.replace(palabra_original, palabra_nueva)):
        print("El contenido fue actualizado correctamente.")

def graficar_vocales_txt(ruta_txt):
    contenido = leer_archivo_txt(ruta_txt)
    if contenido is None:
        return
    vocales = ["a", "e", "i", "o", "u"]
    conteo_vocales = [0] * 5
    for letra in contenido.lower():
        if letra in vocales:
            indice_vocal = vocales.index(letra)
            conteo_vocales[indice_vocal] += 1
    print("\nFrecuencia de vocales:")
    for indice in range(5):
        print(" ", vocales[indice], "→", conteo_vocales[indice])
    if TIENE_MATPLOTLIB:
        plt.bar(vocales, conteo_vocales)
        plt.title("Conteo de vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Cantidad")
        plt.show()
    else:
        print("Gráfico no disponible (matplotlib no instalado)")

def submenu_txt():
    ruta_txt = input("Ruta del archivo de texto: ").strip()
    while True:
        print("\nOpciones TXT: 1) Contar  2) Reemplazar  3) Gráfico de vocales  4) Salir")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            contar_txt(ruta_txt)
            pausar()
        elif opcion == "2":
            reemplazar_txt(ruta_txt)
            pausar()
        elif opcion == "3":
            graficar_vocales_txt(ruta_txt)
            pausar()
        elif opcion == "4":
            break
        else:
            print("Esa opción no es válida.")

# ---------- CSV ----------
def abrir_archivo_csv(ruta_csv):
    try:
        archivo_csv = open(ruta_csv, "r", newline="", encoding="utf-8")
        return archivo_csv, csv.reader(archivo_csv)
    except Exception as error:
        print("No se pudo abrir el archivo:", error)
        return None, None

def mostrar_encabezado_csv(ruta_csv):
    archivo_csv, lector_csv = abrir_archivo_csv(ruta_csv)
    if lector_csv is None:
        return
    contador = 0
    try:
        for fila in lector_csv:
            print(fila)
            contador += 1
            if contador >= 15:
                break
    finally:
        try:
            archivo_csv.close()
        except:
            pass

def leer_todo_csv(ruta_csv):
    archivo_csv, lector_csv = abrir_archivo_csv(ruta_csv)
    if lector_csv is None:
        return None
    filas_csv = []
    try:
        for fila in lector_csv:
            filas_csv.append(fila)
    finally:
        try:
            archivo_csv.close()
        except:
            pass
    return filas_csv

def obtener_indice_columna(encabezados_csv, entrada_usuario):
    if entrada_usuario.isdigit():
        indice = int(entrada_usuario)
        return indice if 0 <= indice < len(encabezados_csv) else -1
    for indice in range(len(encabezados_csv)):
        if encabezados_csv[indice] == entrada_usuario:
            return indice
    return -1

def convertir_columna_a_float(filas_csv, indice_columna):
    valores_numericos = []
    for fila in filas_csv:
        if indice_columna < len(fila):
            texto_valor = fila[indice_columna].strip()
            if texto_valor != "":
                try:
                    valores_numericos.append(float(texto_valor.replace(",", ".")))
                except:
                    pass
    return valores_numericos

def calcular_estadisticas_manuales(valores_numericos):
    cantidad = len(valores_numericos)
    if cantidad == 0:
        return (0, None, None, None, None, None)
    suma = sum(valores_numericos)
    promedio = suma / cantidad
    ordenados = sorted(valores_numericos)
    minimo = ordenados[0]
    maximo = ordenados[-1]
    if cantidad % 2 == 1:
        mediana = ordenados[cantidad // 2]
    else:
        mediana = (ordenados[cantidad // 2 - 1] + ordenados[cantidad // 2]) / 2.0
    suma_cuadrados = sum((x - promedio) ** 2 for x in valores_numericos)
    desviacion = (suma_cuadrados / cantidad) ** 0.5
    return (cantidad, promedio, mediana, desviacion, minimo, maximo)

def mostrar_estadisticas_csv(ruta_csv):
    filas_csv = leer_todo_csv(ruta_csv)
    if not filas_csv:
        print("El archivo CSV está vacío o no se pudo leer.")
        return
    encabezados_csv = filas_csv[0]
    print("\nColumnas disponibles:")
    for indice in range(len(encabezados_csv)):
        print("[" + str(indice) + "] " + encabezados_csv[indice])
    seleccion = input("Escriba el nombre o número de la columna: ").strip()
    indice_columna = obtener_indice_columna(encabezados_csv, seleccion)
    if indice_columna == -1:
        print("No se encontró la columna indicada.")
        return
    valores_numericos = convertir_columna_a_float(filas_csv[1:], indice_columna)
    cantidad, promedio, mediana, desviacion, minimo, maximo = calcular_estadisticas_manuales(valores_numericos)
    print("\nResumen estadístico:")
    print("Cantidad de datos: " + str(cantidad))
    print("Promedio: " + str(promedio))
    print("Mediana: " + str(mediana))
    print("Desviación estándar: " + str(desviacion))
    print("Valor mínimo: " + str(minimo))
    print("Valor máximo: " + str(maximo))

def submenu_csv():
    ruta_csv = input("Ruta del archivo CSV: ").strip()
    while True:
        print("\nOpciones CSV: 1) Ver primeras filas  2) Estadísticas  3) Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_encabezado_csv(ruta_csv)
            pausar()
        elif opcion == "2":
            mostrar_estadisticas_csv(ruta_csv)
            pausar()
        elif opcion == "3":
            break
        else:
            print("Opción no reconocida.")


if __name__=="main_":
    try: main()
    except KeyboardInterrupt:
        print("\nInterrumpido."); sys.exit(0)