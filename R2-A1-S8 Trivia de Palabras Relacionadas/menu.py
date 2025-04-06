#Menu interactivo para clientes#

from tarea import *

def menu_principal():
    lista= ListaSimple()
    while True:
        print("_MENÚ PRINCIPAL_")
        print("1) Insertar clientes ")
        print("2) Listar a la derecha ")
        print("3) Salir")
        opcion= input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Ingrese la cédula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            cliente = Cliente(cedula, nombre)
            lista.insertar_orden(cliente)
            print("Cliente insertado correctamente.")
        elif opcion == "2":
            lista.listar_clientes()
        elif opcion == "3":
            print("Finalizando aplicación")
            break
        else:
            print("Opción no válida, intente nuevamente.")
if __name__ == "__main__":
    menu_principal()