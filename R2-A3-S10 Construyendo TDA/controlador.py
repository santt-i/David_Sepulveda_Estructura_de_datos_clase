from modelo import ListaDobleClientes, Cliente

class ClienteControlador:
    def __init__(self):
        self.lista_clientes = ListaDobleClientes()
    def insertar_cliente(self, cedula, cliente):
        try:
            cedula_int= int(cedula)
            nuevo_cliente = Cliente(cedula, cliente)
            self.lista_clientes.insertar_ordenado(nuevo_cliente)
            return True, f"el cliente {nuevo_cliente.nombre} fue insertado"
        except ValueError:
            return False, "la cedula debe ser un número entero"
    def listar_clientes_derecha(self):
        return self.lista_clientes.listar_clientes_derecha()
    def listar_clientes_izquierda(self):
        return self.lista_clientes.listar_clientes_izquierda()
