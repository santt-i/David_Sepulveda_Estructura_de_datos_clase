import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None  # Apunta al siguiente nodo

class ListaCircular:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio  # Apunta a sí mismo (circular)
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio  # Cierre circular

    def listar_clientes(self):
        if self.inicio is None:
            return "Lista vacía"
        temp = self.inicio
        clientes = []
        while True:
            clientes.append(f"Cédula: {temp.cedula}, Nombre: {temp.nombre}")
            temp = temp.siguiente
            if temp == self.inicio:
                break
        return "\n".join(clientes)


# Clase para la interfaz gráfica
class InterfazListaCircular:
    def __init__(self, root):
        self.lista = ListaCircular()

        # Configuración de la ventana
        root.title("Lista Circular de Clientes")
        root.geometry("500x500")
        root.config(bg="#f2f2f2")  # Color de fondo suave

        # Título de la ventana
        self.title_label = tk.Label(root, text="Gestión de Clientes", font=("Helvetica", 18, "bold"), fg="#4a90e2", bg="#f2f2f2")
        self.title_label.pack(pady=20)

        # Etiquetas y campos de entrada
        self.cedula_label = tk.Label(root, text="Cédula:", font=("Helvetica", 12), bg="#f2f2f2")
        self.cedula_label.pack(pady=5)
        self.cedula_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=25)
        self.cedula_entry.pack(pady=10)

        self.nombre_label = tk.Label(root, text="Nombre:", font=("Helvetica", 12), bg="#f2f2f2")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root, font=("Helvetica", 12), relief="solid", bd=2, width=25)
        self.nombre_entry.pack(pady=10)

        # Botones
        self.insertar_button = tk.Button(root, text="Insertar Cliente", font=("Helvetica", 12), bg="#4a90e2", fg="white", relief="flat", width=20, height=2, command=self.insertar_cliente)
        self.insertar_button.pack(pady=10)

        self.listar_button = tk.Button(root, text="Listar Clientes", font=("Helvetica", 12), bg="#50e3c2", fg="white", relief="flat", width=20, height=2, command=self.listar_clientes)
        self.listar_button.pack(pady=10)

        self.salir_button = tk.Button(root, text="Salir", font=("Helvetica", 12), bg="#f5a623", fg="white", relief="flat", width=20, height=2, command=root.quit)
        self.salir_button.pack(pady=10)

    def insertar_cliente(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        if cedula and nombre:
            self.lista.insertar_cliente(cedula, nombre)
            messagebox.showinfo("Éxito", "Cliente insertado correctamente")
            self.cedula_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese ambos datos")

    def listar_clientes(self):
        clientes = self.lista.listar_clientes()
        messagebox.showinfo("Lista de Clientes", clientes)


# Iniciar la aplicación
root = tk.Tk()
app = InterfazListaCircular(root)
root.mainloop()
