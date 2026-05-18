import sys
sys.path.append("src")

from model.calculadora import Calculadora
from controller.calculadora_controller import CalculadoraController



impuesto= Calculadora(id= "", ingresos_anuales= "",
                            deducciones_generales= "",
                            aporte_pension= "",
                            aporte_salud= "",
                            numero_dependientes= "",
                            tiene_vivienda_propia= False,
                            intereses_credito_vivienda= "" )



impuesto.id= int(input("id : "))
impuesto.ingresos_anuales= float(input("Ingresos anuales : "))
impuesto.deducciones_generales = float(input("Deducciones: "))
impuesto.aporte_pension = float(input("Pensión : "))
impuesto.aporte_salud=float(input("Salud : "))
impuesto.numero_dependientes = int(input("número dependientes: "))
print("Elija la opción:")
print("1. Sí tiene vivienda propia")
print("2. No tiene vivienda propia")
opcion_vivienda = int(input("Opción (1/2): "))
impuesto.tiene_vivienda_propia = opcion_vivienda == 1
if impuesto.tiene_vivienda_propia:
    impuesto.intereses_credito_vivienda = float(input("Interés vivienda: "))

CalculadoraController.insertar( impuesto )

print("Impuesto insertado!")