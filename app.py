import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.c"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title("Simple Text Editor")

def obtenerDatos():
    input = txt_edit.get("1.0",tk.END)
    print(input)

window = tk.Tk()
window.title("Compilador")
window.rowconfigure(1, minsize=300, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

# Inicilizacion de secciones
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_resultados = tk.Frame(window, relief=tk.RAISED, bd=2)

# Inicializacion de botones
btn_open  = tk.Button(fr_buttons, text ="Abrir documento", command = open_file)
btn_ejemplo_correcto  = tk.Button(fr_buttons, text ="Ejemplo correcto", command = open_file)
btn_ejemplo_incorrecto  = tk.Button(fr_buttons, text ="Ejemplo incorrecto", command = open_file)
btn_limpiar  = tk.Button(fr_buttons, text ="Limpiar", command = open_file)
btn_analizar = tk.Button(fr_buttons, text="Analizar", command=obtenerDatos)

# Inicilizacion de objetos en el frame de resultados
labelframe = tk.LabelFrame(fr_resultados, text="Resultados")
labelframe.pack(fill="both", expand="yes")
left = tk.Label(labelframe, text="Inside the LabelFrame")
left.pack()


# Localizacion de botones
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_ejemplo_correcto.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_ejemplo_incorrecto.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_limpiar.grid(row=3, column=0, sticky="ew", padx=5, pady=(100, 5))
btn_analizar.grid(row=4, column=0, sticky="ew", padx=5,pady=5)

# Localizacion de secciones
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
fr_resultados.grid(row=1, column=0, sticky="nsew",columnspan=2)

window.mainloop()
