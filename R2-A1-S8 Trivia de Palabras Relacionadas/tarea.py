"""Crear un menú de opciones con a siguiente estructura:
Insertar cliente: Esta opción permite pedir la cedula y nombre del cliente a ser insertado sobre la lista simple. Esta inserción se deberá realizar de forma ordenada
Listar Clientes hacia la derecha: Esta opción permitirá imprimir los n clientes que han sido cargados sobre la lista doble desde el primer nodo hasta el último nodo
Salir: Esta opción permite finalizar la aplicación."""

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}"
class Nodo_Lista:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None #Primer nodo
    def insertar_orden (self, cliente):
        nodo = Nodo_Lista(cliente)
        #1) Lista Vacia
        if self.cabeza is None:
            self.cabeza = nodo
        #2) Insertar al inicio
        elif cliente.cedula < self.cabeza.cliente.cedula:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo

        #3) Insertar mitad o final
        else:
            actual = self.cabeza
            while actual.siguiente is not None and cliente.cedula > actual.siguiente.cliente.cedula:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo
        #Metodo listar a la derecha
    def listar_clientes(self):
        actual= self.cabeza
        if actual is None:
            print("La lista no tiene elementos")
        else:
            print("__Clientes de la lista__")
            while actual is not None:
                print(actual.cliente)
                actual = actual.siguiente

