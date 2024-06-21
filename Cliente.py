class Cliente:
  def __init__(self,nombre, apellido, id_cliente):
    self.nombre= nombre
    self.apellido= apellido
    self.id_cliente= id_cliente

  def mostrar_info(self):
    return f"Cliente: {self.nombre} {self.apellido}, ID: {self.id_cliente}"