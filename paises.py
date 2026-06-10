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
        print("Error en el formato del CSV, revisa los datos.")


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


# funcion para filtrar paises por continente, rango de poblacion y rango de superficie
def filtrar_paises(paises):
    if len(paises) == 0:
        print("No hay paises cargados todavia.")
        return

    print("\n--- FILTRAR PAISES ---")
    print("(Deja en blanco para omitir un filtro)")

    continente = input("Continente: ").strip()

    try:
        pob_min = input("Poblacion minima: ").strip()
        pob_min = int(pob_min) if pob_min != "" else None

        pob_max = input("Poblacion maxima: ").strip()
        pob_max = int(pob_max) if pob_max != "" else None

        sup_min = input("Superficie minima (km2): ").strip()
        sup_min = int(sup_min) if sup_min != "" else None

        sup_max = input("Superficie maxima (km2): ").strip()
        sup_max = int(sup_max) if sup_max != "" else None

    except ValueError:
        print("Error: ingresa solo numeros en los rangos.")
        return

    resultados = []
    for pais in paises:
        if continente and pais["continente"].strip().lower() != continente.lower():
            continue
        if pob_min is not None and pais["poblacion"] < pob_min:
            continue
        if pob_max is not None and pais["poblacion"] > pob_max:
            continue
        if sup_min is not None and pais["superficie"] < sup_min:
            continue
        if sup_max is not None and pais["superficie"] > sup_max:
            continue
        resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises con esos filtros.")
    else:
        print(f"\n--- RESULTADOS ({len(resultados)} encontrados) ---")
        for pais in resultados:
            print(f"  {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# funcion para ordenar paises por nombre, poblacion o superficie
def ordenar_paises(paises):
    if len(paises) == 0:
        print("No hay paises cargados todavia.")
        return

    print("\n--- ORDENAR PAISES ---")
    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    criterio = input("Elegi una opcion (1-3): ").strip()

    if criterio not in ["1", "2", "3"]:
        print("Opcion invalida.")
        return

    orden = input("Orden ascendente o descendente? (a/d): ").strip().lower()
    if orden not in ["a", "d"]:
        print("Opcion invalida.")
        return

    reverso = orden == "d"

    if criterio == "1":
        paises_ordenados = sorted(paises, key=lambda p: p["nombre"].lower(), reverse=reverso)
        clave = "nombre"
    elif criterio == "2":
        paises_ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=reverso)
        clave = "poblacion"
    else:
        paises_ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=reverso)
        clave = "superficie"

    print(f"\n--- PAISES ORDENADOS POR {clave.upper()} ({'descendente' if reverso else 'ascendente'}) ---")
    for pais in paises_ordenados:
        print(f"  {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# funcion para mostrar estadisticas generales
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises cargados todavia.")
        return

    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) // len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) // len(paises)

    continentes = {}
    for pais in paises:
        c = pais["continente"].strip()
        continentes[c] = continentes.get(c, 0) + 1

    print("\n===== ESTADISTICAS =====")
    print(f"Total de paises: {len(paises)}")
    print(f"Mayor poblacion: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"Menor poblacion: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de poblacion: {promedio_pob}")
    print(f"Promedio de superficie: {promedio_sup} km2")
    print("\nPaises por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente}: {cantidad}")
    print("========================")


# bloque principal
paises = []
opcion = 0

cargar_csv(paises)

while opcion != 7:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            agregar_pais(paises)
        elif opcion == 2:
            actualizar_pais(paises)
        elif opcion == 3:
            buscar_pais(paises)
        elif opcion == 4:
            filtrar_paises(paises)
        elif opcion == 5:
            ordenar_paises(paises)
        elif opcion == 6:
            mostrar_estadisticas(paises)
        elif opcion == 7:
            print("Saliendo del sistema. Hasta luego!")
        else:
            print("Opcion invalida. Ingrese un numero entre 1 y 7.")

    except ValueError as e:
        print(f"Error: {e}")