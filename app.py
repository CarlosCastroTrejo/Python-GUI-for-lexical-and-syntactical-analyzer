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
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open  = tk.Button(fr_buttons, text ="Abrir documento", command = open_file)
btn_analizar = tk.Button(fr_buttons, text="Analizar", command=obtenerDatos)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_analizar.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
