#Lista doblemente enlazada
class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}"


class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente  # Este atributo es un objeto de Cliente
        self.siguiente = None   # Referencia nodo siguiente
        self.anterior = None    # Referencia nodo anterior

class ListaDobleClientes:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista
        self.cola = None    # Último nodo de la lista

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_ordenado(self, cliente):
        nuevo_nodo = Nodo(cliente)

        # Caso la lista está vacía
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            print(f"Cliente {cliente.nombre} insertado (lista estaba vacía).")
            return

        # Caso nueva cédula es menor que la cabeza
        if nuevo_nodo.cliente.cedula < self.cabeza.cliente.cedula:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            print(f"Cliente {cliente.nombre} insertado al inicio.")
            return

        # Caso Insertar en medio o al final
        actual = self.cabeza
        # Avanzar mientras no lleguemos al final Y la cédula del siguiente sea menor que la nueva
        while actual.siguiente is not None and actual.siguiente.cliente.cedula < nuevo_nodo.cliente.cedula:
            actual = actual.siguiente

        # Si siguiente= None, se termino la lista
        if actual.siguiente is None:
            # Insertar al final
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            self.cola = nuevo_nodo # Actualizamos la cola
            print(f"Cliente {cliente.nombre} insertado al final.")
        else:
            # Insertar en medio (antes de actual.siguiente)
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            print(f"Cliente {cliente.nombre} insertado en medio.")


    def listar_clientes_derecha(self):
       #inicio-fin
        if self.esta_vacia():
            print("La lista de clientes está vacía.")
            return

        print("\n--- Listado de Clientes (Inicio a Fin) ---")
        actual = self.cabeza
        contador = 1
        while actual is not None:
            print(f"{contador}. {actual.cliente}")
            actual = actual.siguiente
            contador += 1
        print(" ")

    def listar_clientes_izquierda(self):
       #fin-inicio
        if self.esta_vacia():
            print("La lista de clientes está vacía.")
            return

        print("\n--- Listado de Clientes (Fin a Inicio) ---")
        actual = self.cola
        contador = 1
        while actual is not None:
            print(f"{contador}. {actual.cliente}")
            actual = actual.anterior
            contador += 1
        print(" ")

