import sys
sys.path.append("src")

from model.calculadora import Calculadora
from controller.calculadora_controller import CalculadoraController

try:
    id = int(input("Ingrese el id del impuesto que quiere buscar: "))
    impusto_buscado = CalculadoraController.buscar_impuesto(id) 
    print(  f"Impuesto encontrado:" )
    print(f"Ingresos anuales: {impusto_buscado.ingresos_anuales}")
    print(f"Deducciones: {impusto_buscado.deducciones_generales}")
    print(f"Pensión: {impusto_buscado.aporte_pension}")
    print(f"Salud: {impusto_buscado.aporte_salud}")
    print(f"Dependientes: {impusto_buscado.numero_dependientes}")
    print(f"Interes vivienda: {impusto_buscado.intereses_credito_vivienda}")

except Exception as err:
    print("Error : " )
    print( str( err ) )