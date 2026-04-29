import tkinter as tk
from tkinter import messagebox
import json
import os

productos = []
ventas = []

# ----------- ARCHIVO -----------

def cargar_productos():
    global productos
    if os.path.exists("productos.json"):
        with open("productos.json", "r") as archivo:
            productos = json.load(archivo)
            for p in productos:
                lista_productos.insert(tk.END, f"{p['nombre']} - ${p['precio']}")

def guardar_productos():
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo)

# ----------- FUNCIONES -----------

def agregar_producto():
    nombre = entry_nombre.get()
    try:
        precio = float(entry_precio.get())
    except:
        messagebox.showerror("Error", "Precio inválido")
        return

    if nombre == "":
        messagebox.showerror("Error", "Nombre vacío")
        return

    producto = {"nombre": nombre, "precio": precio}
    productos.append(producto)
    lista_productos.insert(tk.END, f"{nombre} - ${precio}")

    guardar_productos()

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

def vender():
    seleccion = lista_productos.curselection()

    if not seleccion:
        messagebox.showerror("Error", "Seleccione un producto")
        return

    try:
        cantidad = int(entry_cantidad.get())
    except:
        messagebox.showerror("Error", "Cantidad inválida")
        return

    producto = productos[seleccion[0]]
    total = producto["precio"] * cantidad

    ventas.append(total)

    messagebox.showinfo("Venta", f"Total: ${total}")

def total_vendido():
    total = sum(ventas)
    messagebox.showinfo("Total", f"Total vendido: ${total}")

# ----------- INTERFAZ -----------

ventana = tk.Tk()
ventana.title("Sistema de Ventas")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Precio").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=5)

lista_productos = tk.Listbox(ventana)
lista_productos.pack(pady=10)

tk.Label(ventana, text="Cantidad").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Button(ventana, text="Vender", command=vender).pack(pady=5)
tk.Button(ventana, text="Total Vendido", command=total_vendido).pack(pady=5)

# 🔥 Cargar datos al iniciar
cargar_productos()

ventana.mainloop()