# vista.py
import tkinter as tk
from tkinter import ttk, messagebox
from controlador import ClienteControlador

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Gestión de Clientes")
        ventana.geometry("520x430")
        self.centrar_ventana(ventana)
        ventana.configure(bg="#f0f4f8")

        self.controlador = ClienteControlador()

        #Estilos
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("TFrame", background="#f0f4f8")
        estilo.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 10), foreground="#333")
        estilo.configure("TEntry", font=("Segoe UI", 10))
        estilo.configure("TButton",
                         font=("Segoe UI", 10, "bold"),
                         foreground="#ffffff",
                         background="#4a90e2",
                         padding=6)
        estilo.map("TButton", background=[("active", "#357ABD")])

        #Contenedor principal
        marco = ttk.Frame(ventana, padding=15, style="TFrame")
        marco.grid(sticky="nsew")
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=1)

        # Entradas
        self.etiqueta_cedula = ttk.Label(marco, text="Cédula:")
        self.etiqueta_cedula.grid(row=0, column=0, sticky="w")
        self.entrada_cedula = ttk.Entry(marco)
        self.entrada_cedula.grid(row=0, column=1, sticky="ew", pady=2)

        self.etiqueta_nombre = ttk.Label(marco, text="Nombre:")
        self.etiqueta_nombre.grid(row=1, column=0, sticky="w")
        self.entrada_nombre = ttk.Entry(marco)
        self.entrada_nombre.grid(row=1, column=1, sticky="ew", pady=2)

        #Botones
        self.boton_insertar = ttk.Button(marco, text="Insertar Cliente", command=self.insertar_cliente)
        self.boton_insertar.grid(row=2, column=0, columnspan=2, pady=10)

        self.boton_listar_derecha = ttk.Button(marco, text="Listar (Inicio a Fin)", command=self.listar_derecha)
        self.boton_listar_derecha.grid(row=3, column=0, columnspan=2, pady=5)

        self.boton_listar_izquierda = ttk.Button(marco, text="Listar (Fin a Inicio)", command=self.listar_izquierda)
        self.boton_listar_izquierda.grid(row=4, column=0, columnspan=2, pady=5)

        #Separador
        ttk.Separator(marco, orient="horizontal").grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)

        self.etiqueta_lista = ttk.Label(marco, text="Clientes registrados:")
        self.etiqueta_lista.grid(row=6, column=0, columnspan=2, sticky="w")

        #Lista
        self.lista_clientes = tk.Listbox(marco, height=10, font=("Segoe UI", 10),
                                         bg="#ffffff", fg="#333", highlightbackground="#ccc",
                                         relief="solid", borderwidth=1, selectbackground="#d0e3f4")
        self.lista_clientes.grid(row=7, column=0, columnspan=2, sticky="nsew")
        marco.columnconfigure(1, weight=1)
        marco.rowconfigure(7, weight=1)

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        ventana.geometry(f'+{x}+{y}')

    def insertar_cliente(self):
        cedula = self.entrada_cedula.get()
        nombre = self.entrada_nombre.get()
        exito, mensaje = self.controlador.insertar_cliente(cedula, nombre)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.entrada_cedula.delete(0, tk.END)
            self.entrada_nombre.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)

    def listar_derecha(self):
        clientes = self.controlador.listar_clientes_derecha()
        self.actualizar_lista(clientes)

    def listar_izquierda(self):
        clientes = self.controlador.listar_clientes_izquierda()
        self.actualizar_lista(clientes)

    def actualizar_lista(self, clientes):
        self.lista_clientes.delete(0, tk.END)
        for cliente in clientes:
            self.lista_clientes.insert(tk.END, cliente)

def main():
    raiz = tk.Tk()
    app = VentanaPrincipal(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    main()
