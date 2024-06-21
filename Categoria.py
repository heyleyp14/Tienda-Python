class Categoria:
  def __init__(self,nombre):
    self.nombre= nombre

  def mostrar_info(self):
        return f"Categoría: {self.nombre}"