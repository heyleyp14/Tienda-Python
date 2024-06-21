import tkinter as tk
from tkinter import simpledialog, messagebox
from Categoria import Categoria
from Cliente import Cliente
from ItemOrden import ItemOrden
from Orden import Orden
from Producto import Producto
from Tienda import Tienda
from PIL import Image, ImageTk

class TiendaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tienda")
        self.master.configure(bg="#C5CAE9")
        self.master.geometry("400x500")

        self.label = tk.Label(master, text="Bienvenido a la tienda", font=("Arial", 18),bg="#C5CAE9")
        self.label.pack(pady=10)

        self.imagen = Image.open("imagen.png")
        self.imagen = self.imagen.resize((200, 200))
        self.imagen = ImageTk.PhotoImage(self.imagen)

        self.label_imagen = tk.Label(master, image=self.imagen,bg="#C5CAE9")
        self.label_imagen.pack()

        self.tienda = Tienda()

        botones = [
            ("Registrar Producto", self.registrar_producto),
            ("Registrar Cliente", self.registrar_cliente),
            ("Crear Orden", self.crear_orden),
            ("Mostrar Productos", self.mostrar_productos),
            ("Salir", self.salir)
        ]

        max_button_width = max(len(text) for text, _ in botones) + 4 

        button_width = 20 
        button_padx = 10
        button_pady = 5

        for texto, comando in botones:
            btn = tk.Button(master, text=texto, width=max_button_width, command=comando,bg="#E0E0E0",font=("Arial",12))
            btn.pack(pady=button_pady, padx=button_padx)

    def registrar_producto(self):
        nombre = simpledialog.askstring("Registrar Producto", "Ingrese el nombre del producto:")
        precio = float(simpledialog.askstring("Registrar Producto", "Ingrese el precio del producto:"))
        categoria_nombre = simpledialog.askstring("Registrar Producto", "Ingrese la categoría del producto:")
        categoria = Categoria(categoria_nombre)
        producto = Producto(nombre, precio, categoria)
        self.tienda.registrar_producto(producto)
        self.mostrar_info("Registro", "Producto registrado con éxito.")

    def registrar_cliente(self):
        nombre = simpledialog.askstring("Registrar Cliente", "Ingrese el nombre del cliente:")
        apellido = simpledialog.askstring("Registrar Cliente", "Ingrese el apellido del cliente:")
        id_cliente = simpledialog.askstring("Registrar Cliente", "Ingrese el ID del cliente:")
        cliente = Cliente(nombre, apellido, id_cliente)
        self.tienda.registrar_cliente(cliente)
        self.mostrar_info("Registro", "Cliente registrado con éxito.")

    def crear_orden(self):
        id_cliente = simpledialog.askstring("Crear Orden", "Ingrese el ID del cliente:")
        cliente = None
        for c in self.tienda.clientes:
            if c.id_cliente == id_cliente:
                cliente = c
                break
        if cliente is None:
            self.mostrar_info("Error", "Cliente no encontrado.")
            return

        orden = Orden(cliente)
        seguir_agregando = True
        while seguir_agregando:
            nombre_producto = simpledialog.askstring("Agregar Producto", "Ingrese el nombre del producto:")
            cantidad = int(simpledialog.askstring("Agregar Producto", "Ingrese la cantidad:"))
            producto_encontrado = False
            for p in self.tienda.productos:
                if p.nombre == nombre_producto:
                    item = ItemOrden(p, cantidad)
                    orden.agregar_item(item)
                    producto_encontrado = True
                    break
            if not producto_encontrado:
                self.mostrar_info("Error", "Producto no encontrado.")
            respuesta = simpledialog.askstring("Crear Orden", "¿Desea agregar otro producto? (si/no)")
            if respuesta.lower() != "si":
                seguir_agregando = False

        self.tienda.crear_orden(orden)
        self.mostrar_info("Orden", "Orden creada con éxito.")

    def mostrar_productos(self):
        productos_info = "\n".join([p.mostrar_info() for p in self.tienda.productos])
        self.mostrar_info("Productos", productos_info)

    def mostrar_info(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def salir(self):
        self.master.quit()

root = tk.Tk()
app = TiendaGUI(root)
root.mainloop()

