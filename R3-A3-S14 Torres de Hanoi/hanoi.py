import tkinter as tk
from tkinter import ttk, messagebox

class TorresHanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanói - Animación")
        self.root.geometry("800x600")
        self.root.config(bg="#2C3E50")

        self.num_discos = 3
        self.movimientos = []
        self.paso_actual = 0
        self.animando = False
        self.velocidad = 500
        self.discos = []
        self.torres = []

        self.crear_widgets()
        self.actualizar_torres()

    def crear_widgets(self):
        control_frame = tk.Frame(self.root, bg="#34495E", padx=10, pady=10)
        control_frame.pack(fill=tk.X)

        tk.Label(control_frame, text="Discos:", bg="#34495E", fg="white").grid(row=0, column=0)
        self.spin_discos = tk.Spinbox(control_frame, from_=1, to=8, width=5)
        self.spin_discos.grid(row=0, column=1, padx=5)

        ttk.Button(control_frame, text="Resolver", command=self.iniciar_solucion).grid(row=0, column=2, padx=5)
        ttk.Button(control_frame, text="Reiniciar", command=self.actualizar_torres).grid(row=0, column=3, padx=5)

        tk.Label(control_frame, text="Velocidad:", bg="#34495E", fg="white").grid(row=0, column=4)
        self.velocidad_scale = tk.Scale(control_frame, from_=100, to=2000, orient=tk.HORIZONTAL,
                                        bg="#34495E", fg="white", troughcolor="#2C3E50",
                                        command=lambda v: setattr(self, 'velocidad', int(v)))
        self.velocidad_scale.set(self.velocidad)
        self.velocidad_scale.grid(row=0, column=5, padx=10)

        self.canvas = tk.Canvas(self.root, bg="#2C3E50", height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.contador = tk.Label(self.root, text="Movimientos: 0", bg="#2C3E50", fg="white")
        self.contador.pack(side=tk.BOTTOM)

    def crear_torres(self):
        self.canvas.delete("all")
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        base_y = alto - 50
        self.canvas.create_rectangle(50, base_y, ancho - 50, base_y + 10, fill="#7F8C8D", outline="")

        separacion = ancho // 4
        for i in range(3):
            x = separacion * (i + 1)
            self.canvas.create_rectangle(x - 5, 100, x + 5, base_y, fill="#95A5A6", outline="")

    def crear_discos(self):
        self.discos = []
        self.crear_torres()
        ancho_torre = self.canvas.winfo_width() // 4
        colores = ["#E74C3C", "#3498DB", "#2ECC71", "#F1C40F", "#9B59B6", "#1ABC9C", "#E67E22", "#34495E"]

        self.torres = [list(reversed(range(self.num_discos))), [], []]

        for i in range(self.num_discos):
            tamaño = (i + 1) * (ancho_torre // self.num_discos)
            color = colores[i % len(colores)]
            disco = self.canvas.create_rectangle(0, 0, tamaño, 20, fill=color, outline="#2C3E50")
            self.discos.append(disco)

        self.colocar_discos_iniciales()

    def colocar_discos_iniciales(self):
        pos_y = self.canvas.winfo_height() - 70
        separacion = self.canvas.winfo_width() // 4
        for i in reversed(range(self.num_discos)):
            ancho_disco = self.canvas.coords(self.discos[i])[2] - self.canvas.coords(self.discos[i])[0]
            self.canvas.coords(
                self.discos[i],
                separacion - ancho_disco / 2,
                pos_y,
                separacion + ancho_disco / 2,
                pos_y + 20
            )
            pos_y -= 25

    def resolver_hanoi(self, n, origen, auxiliar, destino):
        if n > 0:
            self.resolver_hanoi(n - 1, origen, destino, auxiliar)
            self.movimientos.append((origen, destino))
            self.resolver_hanoi(n - 1, auxiliar, origen, destino)

    def iniciar_solucion(self):
        if self.animando:
            return

        try:
            self.num_discos = int(self.spin_discos.get())
            if self.num_discos < 1 or self.num_discos > 8:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entre 1 y 8")
            return

        self.velocidad = self.velocidad_scale.get()
        self.actualizar_torres()
        self.movimientos = []
        self.resolver_hanoi(self.num_discos, 0, 1, 2)
        self.paso_actual = 0
        self.animando = True
        self.root.after(500, self.mover_siguiente_disco)

    def mover_siguiente_disco(self):
        if not self.movimientos or not self.animando:
            self.animando = False
            return

        origen, destino = self.movimientos[self.paso_actual]
        disco_mover = self.torres[origen].pop()
        self.torres[destino].append(disco_mover)
        self.paso_actual += 1
        self.contador.config(text=f"Movimientos: {self.paso_actual}")

        self.animar_disco(disco_mover, origen, destino)

        if self.paso_actual < len(self.movimientos):
            self.root.after(self.velocidad, self.mover_siguiente_disco)
        else:
            self.animando = False

    def animar_disco(self, disco_index, origen, destino):
        disco_id = self.discos[disco_index]
        coords = self.canvas.coords(disco_id)
        x_origen = (coords[0] + coords[2]) / 2
        y_origen = coords[1]
        separacion = self.canvas.winfo_width() // 4
        x_destino = separacion * (destino + 1)
        y_destino = self.obtener_pos_y(destino)

        self._mover_disco(disco_id, x_origen, y_origen, x_destino, y_destino)

    def _mover_disco(self, disco, x1, y1, x2, y2, pasos=20, delay=10):
        dx = (x2 - x1) / pasos
        dy = (y2 - y1) / pasos

        def mover_paso(paso=0):
            if paso < pasos:
                self.canvas.move(disco, dx, dy)
                self.root.after(delay, lambda: mover_paso(paso + 1))

        mover_paso()

    def obtener_pos_y(self, torre_index):
        separacion = self.canvas.winfo_width() // 4
        x_torre = separacion * (torre_index + 1)
        pos_y = self.canvas.winfo_height() - 70

        alturas = []
        for disco_id in self.discos:
            coords = self.canvas.coords(disco_id)
            cx = (coords[0] + coords[2]) / 2
            if abs(cx - x_torre) < 50:
                alturas.append(coords[1])

        if alturas:
            pos_y = min(alturas) - 25
        return pos_y

    def actualizar_torres(self):
        self.crear_discos()
        self.contador.config(text="Movimientos: 0")
        self.animando = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TorresHanoiGUI(root)
    root.mainloop()
