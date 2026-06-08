import csv

# funcion que carga los paises desde el archivo csv
def cargar_csv(paises):
    try:
        with open("paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
        print(f"Se cargaron {len(paises)} paises correctamente.")
    except FileNotFoundError:
        print("No se encontro el archivo paises.csv.")
    except ValueError:
        print("Error en el formato del CSV, revisá los datos.")


# funcion auxiliar para buscar un pais por nombre exacto
def buscar_indice(paises, nombre):
    for i in range(len(paises)):
        if paises[i]["nombre"].strip().lower() == nombre.strip().lower():
            return i
    return -1

# funcion para mostrar el menu principal
def mostrar_menu():
    print("\n===== GESTION DE PAISES =====")
    print("1. Agregar pais")
    print("2. Actualizar poblacion y superficie")
    print("3. Buscar pais por nombre")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Ver estadisticas")
    print("7. Salir")
    print("==============================")


# funcion para agregar un pais nuevo
def agregar_pais(paises):
    try:
        nombre = input("Nombre del pais: ")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")
        if buscar_indice(paises, nombre) != -1:
            raise ValueError("Ya existe un pais con ese nombre.")

        poblacion = int(input("Poblacion: "))
        if poblacion < 0:
            raise ValueError("La poblacion no puede ser negativa.")

        superficie = int(input("Superficie en km2: "))
        if superficie < 0:
            raise ValueError("La superficie no puede ser negativa.")

        continente = input("Continente: ")
        if continente.strip() == "":
            raise ValueError("El continente no puede estar vacio.")

        pais = {
            "nombre": nombre.strip(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente.strip()
        }
        paises.append(pais)
        print(f"Pais '{nombre}' agregado correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


# funcion para actualizar poblacion y superficie
def actualizar_pais(paises):
    if len(paises) == 0:
        print("No hay paises cargados todavia.")
        return

    nombre = input("Ingrese el nombre del pais a actualizar: ")
    indice = buscar_indice(paises, nombre)

    if indice == -1:
        print(f"No se encontro el pais '{nombre}'.")
        return

    try:
        poblacion = int(input(f"Nueva poblacion para '{paises[indice]['nombre']}': "))
        if poblacion < 0:
            raise ValueError("La poblacion no puede ser negativa.")

        superficie = int(input(f"Nueva superficie para '{paises[indice]['nombre']}': "))
        if superficie < 0:
            raise ValueError("La superficie no puede ser negativa.")

        paises[indice]["poblacion"] = poblacion
        paises[indice]["superficie"] = superficie
        print("Datos actualizados correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


# funcion para buscar pais por nombre (parcial o exacta)
def buscar_pais(paises):
    if len(paises) == 0:
        print("No hay paises cargados todavia.")
        return

    nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
    resultados = []

    for pais in paises:
        if nombre.strip().lower() in pais["nombre"].strip().lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"No se encontraron paises con '{nombre}'.")
    else:
        print(f"\n--- RESULTADOS ({len(resultados)} encontrados) ---")
        for pais in resultados:
            print(f"  {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")