class Ingresos:
    def __init__(self):
        self.listIngresos = []

    def guardarIngreso(self,id, monto):
        ingresoGuardado = (id, monto)
        self.listIngresos.append(ingresoGuardado)
        return self.listIngresos
    
    def reportIngresos(self):
        dinero = 0
        for ingreso in self.listIngresos:
            dinero = dinero + float(ingreso[1])
    
    def visualizarIngresos(self):
        for ingreso in self.listIngresos:
            print(f"Id: {ingreso[0]} Monto: {ingreso[1]}")

    
