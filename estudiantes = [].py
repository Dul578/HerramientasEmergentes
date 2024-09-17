estudiantes = []

def insertar():
    estudiantes.append({
        "nombre": input("Nombre: "),
        "cali1": float(input("Cali 1: ")),
        "cali2": float(input("Cali 2: ")),
        "cali3": float(input("Cali 3: "))
    })
    print("Estudiante insertado correctamente.\n")

def mostrar():
    if estudiantes:
        for i, e in enumerate(estudiantes):
            prom = (e['cali1'] + e['cali2'] + e['cali3']) / 3
            print(f"{i}: {e['nombre']} - {e['cali1']}, {e['cali2']}, {e['cali3']} | Prom: {prom:.2f}")
        print()
    else:
        print("No hay estudiantes registrados.\n")

def actualizar():
    mostrar()
    idx = int(input("ID del estudiante a actualizar: "))
    if 0 <= idx < len(estudiantes):
        estudiantes[idx] = {
            "nombre": input("Nuevo nombre: "),
            "cali1": float(input("Nueva Cali 1: ")),
            "cali2": float(input("Nueva Cali 2: ")),
            "cali3": float(input("Nueva Cali 3: "))
        }
        print("Estudiante actualizado correctamente.\n")
    else:
        print("ID no válido.\n")

def eliminar():
    mostrar()
    idx = int(input("ID del estudiante a eliminar: "))
    if 0 <= idx < len(estudiantes):
        estudiantes.pop(idx)
        print("Estudiante eliminado correctamente.\n")
    else:
        print("ID no válido.\n")

# Menú principal
while True:
    op = input("1-Insertar, 2-Mostrar, 3-Actualizar, 4-Eliminar, 5-Salir: ")
    if op == '1': insertar()
    elif op == '2': mostrar()
    elif op == '3': actualizar()
    elif op == '4': eliminar()
    elif op == '5': break
    else:
        print("Opción no válida.\n")