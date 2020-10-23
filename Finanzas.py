from Ingresos import Ingresos
from Egresos import Egresos

Ingresos = Ingresos()
Egresos = Egresos()

class Finanzas:

    def __init__(self, id, monto):
        self.id = id
        self.monto = monto

    def cantidadFinal(self):
        dineroRetirado = Egresos.reportEgresos()
        dineroIntroducido = Ingresos.reportIngresos()
        dineroFinal = (dineroIntroducido + self.monto - dineroRetirado)
        return dineroFinal    

    def saveEgreso(self, id, monto):
        Egresos.guardarEgreso(id, monto)

    def visualizarEgresos(self):
        Egresos.visualizarEgresos()

    def saveIngreso(self, id, monto):
        Ingresos.guardarIngreso(id, monto)

    def visualizarIngresos(self):
        Ingresos.visualizarIngreso()

    def reportTransacciones(self):
        Egresos.visualizarEgresos()
        Ingresos.visualizarIngresos()
    


    


    