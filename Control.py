from Finanzas import Finanzas

while True:
    print('Bienvenido/a')
    print('Registrar una cuenta con monto igual a $0.00. (Registrar Cuenta)')
    print('Monto dentro de la cuenta. (Monto)')
    print('Reporte de transacciones.(Reporte de Transacciones)')
    print('Meter dinero a cuenta. (Ingreso)')
    print('Retirar dinero de la cuenta. (Egreso)')
    print('Reporte de ingresos. (Reporte de ingresos)')
    print('Reporte de egresos. (Reporte de egresos)')
    print('Terminar sesión. (Salir)')
    accion = input('Escriba la descripición entre paréntesis de la acción de su preferencia: ')

    if accion == 'Registrar Cuenta':
        monto = 0
        id = input("Escriba la identificación de su cuenta: ")
        nuevaCuenta = Finanzas(id, monto)
         print('----------------------------')
        print('Su cuenta ha sido creada con éxito')
    
    elif accion == 'Monto':
        dineroCuenta = Finanzas.cantidadFinal()
         print('----------------------------')
        print('${Finanzas.cantidad}')

    elif accion == 'Reporte de Transacciones':
        print('----------------------------')
        print('Su reporte de transacciones es el siguiente: ')
        print('Ingresos: ')
        Finanzas.visualizarIngresos()
        print('Egresos: ')
        Finanzas.visualizarEgresos

    elif accion == 'Salir':
        break
    
