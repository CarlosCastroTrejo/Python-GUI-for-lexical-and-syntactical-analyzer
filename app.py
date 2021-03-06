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
    window.title("Compilador")

def analizar_texto():
    txt_resultado_compilado['state']=tk.NORMAL
    txt_resultado_compilado.delete(1.0, tk.END)
    txt_resultado_compilado['state']=tk.DISABLED
    text = txt_edit.get(1.0,tk.END)
    text=text.lstrip()
    text=text.rstrip()
    resultados=''

    if(text!=''):
        result, error = basic.run('<stdin>', text)
        if error: 
            label_mensaje['text'] = 'Mensaje: Error - '+error.as_string()    
        elif result:
            if len(result.elements) == 1:
                resultados=repr(result.elements[0])
                print(repr(result.elements[0]))
            else:
                resultados=repr(result)
                print(repr(result))
            
            label_mensaje['text'] = 'Mensaje: Todo cool :)'  
            txt_resultado_compilado['state']=tk.NORMAL
            txt_resultado_compilado.insert(1.0,resultados)
            txt_resultado_compilado['state']=tk.DISABLED
    else:
        label_mensaje['text'] = 'Mensaje: Texto vacío'


def limpiar_texto():
    txt_edit.delete(1.0, tk.END)

def cargar_archivo_incorrecto():
    txt_edit.delete(1.0, tk.END)
    filepath='./codigo_incorrecto.txt'
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

def cargar_archivo_correcto():
    txt_edit.delete(1.0, tk.END)
    filepath='./codigo_correcto.txt'
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

window = tk.Tk()
window.title("Compilador")
window.rowconfigure(1, minsize=300, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

# Inicilizacion de secciones
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_resultad_mensajes=tk.Frame(window,relief=tk.RAISED,bd=2)
txt_resultado_compilado=tk.Text(window,relief=tk.RAISED, state=tk.DISABLED,bd=2)


# Inicializacion de botones
btn_open  = tk.Button(fr_buttons, text ="Abrir documento", command = abrir_archivo)
btn_ejemplo_correcto  = tk.Button(fr_buttons, text ="Ejemplo correcto", command = cargar_archivo_correcto)
btn_ejemplo_incorrecto  = tk.Button(fr_buttons, text ="Ejemplo incorrecto", command = cargar_archivo_incorrecto)
btn_limpiar  = tk.Button(fr_buttons, text ="Limpiar", command = limpiar_texto)
btn_analizar = tk.Button(fr_buttons, text="Analizar", command=analizar_texto)

# Inicializacion de Mensajes
label_mensaje = tk.Label(fr_resultad_mensajes, text="Mensaje: ")
label_lineas_analizadas = tk.Label(fr_resultad_mensajes, text="Lineas analizadas: ")


# Localizacion de botones
btn_open.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)
btn_ejemplo_correcto.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
btn_ejemplo_incorrecto.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)
btn_limpiar.grid(row=3, column=0, sticky="nesw", padx=5, pady=(100, 5))
btn_analizar.grid(row=4, column=0, sticky="nesw", padx=5,pady=5)

# Localizacion de etiquetas y secciones en resultado
label_mensaje.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)
label_lineas_analizadas.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)

fr_resultad_mensajes.grid(row=1, column=0, sticky="nesw")
txt_resultado_compilado.grid(row=1, column=1, sticky="nesw")


# Localizacion de secciones
fr_buttons.grid(row=0, column=0, sticky="nesw")
txt_edit.grid(row=0, column=1, sticky="nesw")


window.mainloop()
