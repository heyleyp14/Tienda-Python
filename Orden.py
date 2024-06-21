class Orden:
  def __init__(self,cliente):
    self.cliente= cliente
    self.items= []
    self.total= 0

  def agregar_item(self,item):
    self.items.append(item)

  def calcular_total(self):
     total = 0
     for item in self.items:
       total += item.calcular_subtotal()
     self.total = total