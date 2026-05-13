import unittest
import sys
sys.path.append( "src" )

from model.calculadora import Calculadora
from controller.calculadora_controller import CalculadoraController

class TestCalculadoraImpuestos( unittest.TestCase ):

    def setUpClass():
        """ Test Fixtures que se ejecuta al inicio de las pruebas solamente"""
        CalculadoraController.borrar_tabla()
        CalculadoraController.crear_tabla()

    def test_insert_1(self):
        # Crear una compra de credito
        impuesto = Calculadora( id= 1,ingresos_anuales= 80_000_000,
                            deducciones_generales= 10_000_000,
                            aporte_pension= 6_400_000,
                            aporte_salud= 3_200_000,
                            numero_dependientes= 2,
                            tiene_vivienda_propia= True,
                            intereses_credito_vivienda= 5_000_000  )

        
        # Guardarla en la BD
        CalculadoraController.insertar( impuesto )
        
        # Buscarla
        impuesto_buscar = CalculadoraController.buscar_impuesto( impuesto.id )
        
        # Verificar si la trajo bien
        self.assertTrue(  impuesto.is_equal( impuesto_buscar )  )

if __name__ == '__main__':
    unittest.main()        