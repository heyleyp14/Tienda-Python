class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_orden(self, orden):
        orden.calcular_total()
        self.ordenes.append(orden)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.mostrar_info())