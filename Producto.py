class Producto:
  def __init__(self,nombre, precio, categoria):
    self.nombre= nombre
    self.precio= precio
    self.categoria= categoria

  def mostrar_info(self):
    return f"Producto: {self.nombre}, Precio: {self.precio}, {self.categoria.mostrar_info()}"