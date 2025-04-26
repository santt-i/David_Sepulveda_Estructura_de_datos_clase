
class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}"


class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None
        self.anterior = None


class ListaDobleClientes:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_ordenado(self, cliente):
        nuevo_nodo = Nodo(cliente)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return

        if nuevo_nodo.cliente.cedula < self.cabeza.cliente.cedula:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.cliente.cedula < nuevo_nodo.cliente.cedula:
            actual = actual.siguiente

        if actual.siguiente is None:
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo

    def listar_clientes_derecha(self):
        clientes = []
        actual = self.cabeza
        while actual is not None:
            clientes.append(str(actual.cliente))
            actual = actual.siguiente
        return clientes

    def listar_clientes_izquierda(self):
        clientes = []
        actual = self.cola
        while actual is not None:
            clientes.append(str(actual.cliente))
            actual = actual.anterior
        return clientes