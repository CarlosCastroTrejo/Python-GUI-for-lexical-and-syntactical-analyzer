import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import basic 

# Abrir un documento
def abrir_archivo():
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title("Simple Text Editor")

def analizar_texto():
    text = txt_edit.get("1.0",tk.END)
    text=text.lstrip()
    text=text.rstrip()
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)

def limpiar_texto():
    txt_edit.delete(1.0, tk.END)

window = tk.Tk()
window.title("Compilador")
window.rowconfigure(1, minsize=300, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

# Inicilizacion de secciones
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_resultados = tk.Frame(window, relief=tk.RAISED, bd=2)


# Inicializacion de botones
btn_open  = tk.Button(fr_buttons, text ="Abrir documento", command = abrir_archivo)
btn_ejemplo_correcto  = tk.Button(fr_buttons, text ="Ejemplo correcto", command = analizar_texto)
btn_ejemplo_incorrecto  = tk.Button(fr_buttons, text ="Ejemplo incorrecto", command = analizar_texto)
btn_limpiar  = tk.Button(fr_buttons, text ="Limpiar", command = limpiar_texto)
btn_analizar = tk.Button(fr_buttons, text="Analizar", command=analizar_texto)

# Inicializacion de Mensajes
label_resultado = tk.Label(fr_resultados, text="Resultado: ")
label_mensaje = tk.Label(fr_resultados, text="Mensaje: ")
label_lineas_analizadas = tk.Label(fr_resultados, text="Lineas analizadas: ")


# Localizacion de botones
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_ejemplo_correcto.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_ejemplo_incorrecto.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_limpiar.grid(row=3, column=0, sticky="ew", padx=5, pady=(100, 5))
btn_analizar.grid(row=4, column=0, sticky="ew", padx=5,pady=5)

label_resultado.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
label_mensaje.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
label_lineas_analizadas.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


# Localizacion de secciones
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
fr_resultados.grid(row=1, column=0, sticky="nsew",columnspan=2)

window.mainloop()
