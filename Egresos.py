class Egresos:
    def __init__(self):
        self.listEgresos = []

    def guardarEgreso(self, id, monto):
        egresoGuardado = (id, monto)
        self.listEgresos.append(egresoGuardado)

    def reportEgresos(self):
        dinero = 0
        for egreso in self.listEgresos:
            dinero = dinero + float(ingreso[1])

    def visualizarEgresos(self):
        for egreso in self.listEgresos:
            print(f"Id: {egreso[0]} Monto: {egreso[1]}")