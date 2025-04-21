from app import *
def main():

    lista_clientes = ListaDobleClientes() # Instancia de la lista

    while True:
        # Mostrar menú
        print("\n--- Menú de Opciones ---")
        print("1. Insertar Cliente (Ordenado por Cédula)")
        print("2. Listar Clientes (Inicio a Fin)")
        print("3. Listar Clientes (Fin a Inicio)")
        print("4. Salir")
        print("------------------------")

        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                try:
                    cedula_str = input("Ingrese la cédula del cliente: ")
                    # Validar que la cédula sea numérica
                    if not cedula_str.isdigit():
                        print("Error: La cédula debe ser un número entero.")
                        continue
                    cedula = int(cedula_str)
                    nombre = input("Ingrese el nombre del cliente: ")
                    if not nombre: # Validar que el nombre no esté vacío
                         print("Error: El nombre no puede estar vacío.")
                         continue

                    nuevo_cliente = Cliente(cedula, nombre)
                    lista_clientes.insertar_ordenado(nuevo_cliente)

                except ValueError:
                    print("Error: La cédula debe ser un número entero válido.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            case "2":
                lista_clientes.listar_clientes_derecha()

            case "3":
                lista_clientes.listar_clientes_izquierda()

            case "4":
                print("Saliendo de la aplicación...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()