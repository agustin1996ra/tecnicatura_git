""" Ejercicio 4: Calculadora de impuestos
Crear una función para calcular el total de un pago incluyendo
un impuesto aplicado. (IVA)
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
Proporcione el pago sin impuestos: 1000
Proporcione el monto del impuesto: 21%
Pago con impuesto: XXXX
"""


def calculadora_imp(pago_sin_imp, imp):
    return pago_sin_imp + pago_sin_imp * (imp/100)


psi = int(input('Proporcione el pago sin impuestos: '))
impuesto = int(input('Proporcione el porcentaje del impuesto: '))
print(f'Pago con impuesto: {calculadora_imp(psi, impuesto)}')
