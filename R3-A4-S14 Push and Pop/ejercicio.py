
bicola = []

def menu():
    print("\nMenú - Bicola")
    print("1. Insertar por la derecha")
    print("2. Insertar por la izquierda")
    print("3. Atender por la derecha")
    print("4. Atender por la izquierda")
    print("5. Listar elementos")
    print("6. Salir")

def insertar_derecha(dato):
    bicola.append(dato)
    print(f"Elemento '{dato}' insertado por la derecha.")

def insertar_izquierda(dato):
    bicola.insert(0, dato)
    print(f"Elemento '{dato}' insertado por la izquierda.")

def atender_derecha():
    if bicola:
        eliminado = bicola.pop()
        print(f"Elemento '{eliminado}' atendido por la derecha.")
    else:
        print("La bicola está vacía. No hay elementos para atender por la derecha.")

def atender_izquierda():
    if bicola:
        eliminado = bicola.pop(0)
        print(f"Elemento '{eliminado}' atendido por la izquierda.")
    else:
        print("La bicola está vacía. No hay elementos para atender por la izquierda.")

def listar_elementos():
    if bicola:
        print("Elementos en la bicola:")
        for elemento in bicola:
            print(elemento, end=' <- ')
        print("[Frente]")
    else:
        print("La bicola está vacía.")

# === Programa principal ===
while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            dato = input("Ingrese el elemento a insertar por la derecha: ")
            insertar_derecha(dato)
        elif opcion == 2:
            dato = input("Ingrese el elemento a insertar por la izquierda: ")
            insertar_izquierda(dato)
        elif opcion == 3:
            atender_derecha()
        elif opcion == 4:
            atender_izquierda()
        elif opcion == 5:
            listar_elementos()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Ingrese solo números para seleccionar una opción.")