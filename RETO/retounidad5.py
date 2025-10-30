import os, csv
import matplotlib.pyplot as plt

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
            print(" •", nombre_archivo)
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
    total_palabras = len(palabras)
    caracteres_con_espacios = len(contenido)
    caracteres_sin_espacios = sum(1 for caracter in contenido if not caracter.isspace())
    print("\nTotal de palabras:", total_palabras)
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
            conteo_vocales[vocales.index(letra)] += 1
    print("\nFrecuencia de vocales:")
    for i in range(5):
        print(f" {vocales[i]} → {conteo_vocales[i]}")
    plt.bar(vocales, conteo_vocales, color="skyblue")
    plt.title("Conteo de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Cantidad")
    plt.show()

def submenu_txt():
    ruta_txt = input("Ruta del archivo de texto: ").strip()
    while True:
        print("\nOpciones TXT: 1) Contar  2) Reemplazar  3) Gráfico de vocales  4) Volver")
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
    for codificacion in ["utf-8", "latin-1", "cp1252"]:
        try:
            archivo_csv = open(ruta_csv, "r", newline="", encoding=codificacion, errors="replace")
            lector_csv = csv.reader(archivo_csv, delimiter=";")  # ← separador corregido
            return archivo_csv, lector_csv
        except Exception:
            continue
    print("No se pudo abrir el archivo con ninguna codificación compatible.")
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
    filas = []
    try:
        for fila in lector_csv:
            filas.append(fila)
    finally:
        try:
            archivo_csv.close()
        except:
            pass
    return filas

def obtener_indice_columna(encabezados, entrada):
    if entrada.isdigit():
        indice = int(entrada)
        return indice if 0 <= indice < len(encabezados) else -1
    for i, nombre in enumerate(encabezados):
        if nombre == entrada:
            return i
    return -1

def convertir_columna_a_float(filas, indice_columna):
    valores = []
    for fila in filas:
        if indice_columna < len(fila):
            texto = fila[indice_columna].strip()
            if texto != "":
                try:
                    valores.append(float(texto.replace(",", ".")))
                except:
                    pass
    return valores

def calcular_estadisticas(valores):
    cantidad = len(valores)
    if cantidad == 0:
        return (0, None, None, None, None, None)
    suma = sum(valores)
    promedio = suma / cantidad
    valores_ordenados = sorted(valores)
    minimo = valores_ordenados[0]
    maximo = valores_ordenados[-1]
    if cantidad % 2 == 1:
        mediana = valores_ordenados[cantidad // 2]
    else:
        mediana = (valores_ordenados[cantidad // 2 - 1] + valores_ordenados[cantidad // 2]) / 2
    suma_cuadrados = sum((x - promedio) ** 2 for x in valores)
    desviacion = (suma_cuadrados / cantidad) ** 0.5
    return (cantidad, promedio, mediana, desviacion, minimo, maximo)

def mostrar_estadisticas_csv(ruta_csv):
    filas = leer_todo_csv(ruta_csv)
    if not filas:
        print("CSV vacío o no válido.")
        return
    encabezados = filas[0]
    print("\nEncabezados:")
    for i, nombre in enumerate(encabezados):
        print(f"  [{i}] {nombre}")
    seleccion = input("Nombre o índice de columna: ").strip()
    indice = obtener_indice_columna(encabezados, seleccion)
    if indice == -1:
        print("Columna no encontrada.")
        return
    valores = convertir_columna_a_float(filas[1:], indice)
    cantidad, promedio, mediana, desviacion, minimo, maximo = calcular_estadisticas(valores)
    print("\nCantidad:", cantidad)
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)

def graficar_columna_csv(ruta_csv):
    filas = leer_todo_csv(ruta_csv)
    if not filas:
        print("CSV vacío o no válido.")
        return
    encabezados = filas[0]
    print("\nEncabezados:")
    for i, nombre in enumerate(encabezados):
        print(f"  [{i}] {nombre}")
    seleccion = input("Columna numérica (nombre o índice): ").strip()
    indice = obtener_indice_columna(encabezados, seleccion)
    if indice == -1:
        print("Columna no encontrada.")
        return

    valores = convertir_columna_a_float(filas[1:], indice)
    if not valores:
        print("No hay datos numéricos válidos.")
        return

    # Dispersión
    plt.figure()
    plt.scatter(range(len(valores)), valores)
    plt.title(f"Dispersión - {encabezados[indice]}")
    plt.xlabel("Índice")
    plt.ylabel(encabezados[indice])
    plt.show()

    # Barras por rangos
    minimo, maximo = min(valores), max(valores)
    bins = 5
    ancho = (maximo - minimo) / bins if bins > 0 else 1
    etiquetas = []
    frecuencias = [0] * bins
    for b in range(bins):
        limite_inferior = minimo + b * ancho
        limite_superior = minimo + (b + 1) * ancho if b < bins - 1 else maximo
        etiquetas.append(f"{limite_inferior:.2f}-{limite_superior:.2f}")

    for valor in valores:
        for b in range(bins):
            partes = etiquetas[b].split("-")
            li = float(partes[0])
            ls = float(partes[1])
            if li <= valor < ls or (b == bins - 1 and valor <= ls):
                frecuencias[b] += 1
                break

    plt.figure()
    plt.bar(etiquetas, frecuencias, color="mediumseagreen")
    plt.title(f"Barras por rangos - {encabezados[indice]}")
    plt.xlabel("Rango")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def submenu_csv():
    ruta_csv = input("Ruta del archivo CSV: ").strip()
    while True:
        print("\nOpciones CSV: 1) Ver primeras filas  2) Estadísticas  3) Graficar columna  4) Volver")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_encabezado_csv(ruta_csv)
            pausar()
        elif opcion == "2":
            mostrar_estadisticas_csv(ruta_csv)
            pausar()
        elif opcion == "3":
            graficar_columna_csv(ruta_csv)
            pausar()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
            pausar()
def main():
    while True:
        limpiar_pantalla()
        print("\n--- Menú principal ---")
        print("1) Mostrar archivos")
        print("2) Procesar archivo TXT")
        print("3) Procesar archivo CSV")
        print("4) Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_archivos()
            pausar()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
            pausar()

if __name__ == "__main__":
    main()
