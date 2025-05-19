import tkinter as tk
from tkinter import messagebox, ttk

class TorresHanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanói - Animación")
        self.root.geometry("800x600")
        self.root.config(bg="#2C3E50")
        
        # Variables de control
        self.num_discos = 3
        self.movimientos = []
        self.paso_actual = 0
        self.animando = False
        self.velocidad = 500  # ms entre movimientos
        
        # Configurar interfaz
        self.crear_widgets()
        self.actualizar_torres()
    
    def crear_widgets(self):
        # Marco de controles
        control_frame = tk.Frame(self.root, bg="#34495E", padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        
        # Entrada para número de discos
        tk.Label(control_frame, text="Discos:", bg="#34495E", fg="white").grid(row=0, column=0)
        self.spin_discos = tk.Spinbox(control_frame, from_=1, to=8, width=5)
        self.spin_discos.grid(row=0, column=1, padx=5)
        
        # Botones
        ttk.Button(control_frame, text="Resolver", command=self.iniciar_solucion).grid(row=0, column=2, padx=5)
        ttk.Button(control_frame, text="Reiniciar", command=self.actualizar_torres).grid(row=0, column=3, padx=5)
        
        # Control de velocidad
        tk.Label(control_frame, text="Velocidad:", bg="#34495E", fg="white").grid(row=0, column=4)
        self.velocidad_scale = tk.Scale(control_frame, from_=100, to=2000, orient=tk.HORIZONTAL,
                                      bg="#34495E", fg="white", troughcolor="#2C3E50",
                                      command=lambda v: setattr(self, 'velocidad', int(v)))
        self.velocidad_scale.set(self.velocidad)
        self.velocidad_scale.grid(row=0, column=5, padx=10)
        
        # Canvas para torres
        self.canvas = tk.Canvas(self.root, bg="#2C3E50", height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Contador de movimientos
        self.contador = tk.Label(self.root, text="Movimientos: 0", bg="#2C3E50", fg="white")
        self.contador.pack(side=tk.BOTTOM)
    
    def crear_torres(self):
        self.canvas.delete("all")
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        
        # Dibujar bases
        base_y = alto - 50
        self.canvas.create_rectangle(50, base_y, ancho-50, base_y+10, fill="#7F8C8D", outline="")
        
        # Dibujar postes
        separacion = ancho // 4
        for i in range(3):
            x = separacion * (i + 1)
            self.canvas.create_rectangle(x-5, 100, x+5, base_y, fill="#95A5A6", outline="")
    
    def crear_discos(self):
        self.discos = []
        ancho_torre = self.canvas.winfo_width() // 4
        colores = ["#E74C3C", "#3498DB", "#2ECC71", "#F1C40F", "#9B59B6", "#1ABC9C", "#E67E22", "#34495E"]
        
        for i in range(self.num_discos):
            tamaño = (i + 1) * (ancho_torre // self.num_discos)
            color = colores[i % len(colores)]
            disco = self.canvas.create_rectangle(0, 0, tamaño, 20, fill=color, outline="#2C3E50")
            self.discos.insert(0, disco)  # Disco más grande primero
        
        # Posicionar discos en la primera torre
        pos_y = self.canvas.winfo_height() - 70
        separacion = self.canvas.winfo_width() // 4
        for disco in self.discos:
            x0, y0, x1, y1 = self.canvas.coords(disco)
            ancho = x1 - x0
            self.canvas.coords(disco, 
                             separacion - ancho/2, pos_y,
                             separacion + ancho/2, pos_y + 20)
            pos_y -= 25
    
    def mover_disco_animacion(self, origen, destino):
        if not self.movimientos:
            return
        
        # Obtener siguiente movimiento
        movimiento = self.movimientos[self.paso_actual]
        self.paso_actual += 1
        self.contador.config(text=f"Movimientos: {self.paso_actual}")
        
        # Obtener disco a mover
        disco = self.discos[-movimiento[0]]  # El primer disco es el más pequeño
        
        # Animación de movimiento
        x_origen = self.canvas.winfo_width() // 4 * (['A', 'B', 'C'].index(movimiento[1]) + 1)
        x_destino = self.canvas.winfo_width() // 4 * (['A', 'B', 'C'].index(movimiento[2]) + 1)
        
        # Posición actual del disco
        x0, y0, x1, y1 = self.canvas.coords(disco)
        current_x = (x0 + x1) / 2
        
        # Mover hacia arriba
        self.animar_movimiento(disco, current_x, y0, current_x, 100, self.velocidad//2)
        # Mover horizontalmente
        self.animar_movimiento(disco, current_x, 100, x_destino, 100, self.velocidad//2)
        # Mover hacia abajo
        self.animar_movimiento(disco, x_destino, 100, x_destino, self.obtener_pos_y(destino), self.velocidad//2)
        
        # Programar siguiente movimiento
        if self.paso_actual < len(self.movimientos):
            self.root.after(self.velocidad, self.mover_disco_animacion, origen, destino)
        else:
            self.animando = False
    
    def animar_movimiento(self, disco, x0, y0, x1, y1, duracion):
        pasos = duracion // 20
        dx = (x1 - x0) / pasos
        dy = (y1 - y0) / pasos
        
        for i in range(pasos):
            self.canvas.move(disco, dx, dy)
            self.canvas.update()
            self.canvas.after(20)
    
    def obtener_pos_y(self, torre):
        # Obtener posición Y para colocar el disco en la torre
        pos_y = self.canvas.winfo_height() - 70
        for disco in reversed(self.discos):
            x0, y0, x1, y1 = self.canvas.coords(disco)
            if self.canvas.coords(disco)[0] // (self.canvas.winfo_width() // 4) == ['A', 'B', 'C'].index(torre):
                pos_y = y0 - 25
                break
        return pos_y
    
    def resolver_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            self.movimientos.append((n, origen, destino))
            return
        self.resolver_hanoi(n-1, origen, destino, auxiliar)
        self.movimientos.append((n, origen, destino))
        self.resolver_hanoi(n-1, auxiliar, origen, destino)
    
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
        
        self.actualizar_torres()
        self.movimientos = []
        self.resolver_hanoi(self.num_discos, 'A', 'B', 'C')
        self.paso_actual = 0
        self.animando = True
        self.mover_disco_animacion('A', 'C')
    
    def actualizar_torres(self):
        self.crear_torres()
        self.crear_discos()
        self.movimientos = []
        self.paso_actual = 0
        self.contador.config(text="Movimientos: 0")
        self.animando = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TorresHanoiGUI(root)
    root.mainloop()