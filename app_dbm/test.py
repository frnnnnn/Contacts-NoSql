import tkinter as tk
from tkinter import ttk

def create_scrollable_container(root):
    # Crear un widget de contenedor
    container = ttk.Frame(root)
    container.pack(fill=tk.BOTH, expand=True)

    # Crear un widget de scrollbar
    scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Crear un widget de lienzo (Canvas) dentro del contenedor
    canvas = tk.Canvas(container, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configurar la scrollbar para el lienzo
    scrollbar.configure(command=canvas.yview)

    # Agregar contenido al lienzo
    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    for i in range(100):
        label = ttk.Label(frame, text=f"Item {i}")
        label.pack()

    # Configurar el desplazamiento del lienzo
    def on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_canvas_configure)

# Crear la ventana principal
root = tk.Tk()

# Crear el contenedor scrollable
create_scrollable_container(root)

# Iniciar el bucle principal
root.mainloop()
