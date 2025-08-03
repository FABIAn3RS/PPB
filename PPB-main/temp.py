import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.geometry("400x300")

# Cargar imagen desde archivo
imagen = Image.open("fondo.jpg")  # Puedes usar .png también

# Redimensionar si es necesario
imagen = imagen.resize((200, 150))

# Convertir para tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Mostrar en un Label
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

ventana.mainloop()
