import unittest
import sys
sys.path.append( "src" )

from model.calculadora import Calculadora
from controller.calculadora_controller import CalculadoraController

class TestCalculadoraImpuestos( unittest.TestCase ):

    def setUpClass():

        CalculadoraController.borrar_tabla()
        CalculadoraController.crear_tabla()

    def test_insert(self):
  
        impuesto = Calculadora( id= 1,ingresos_anuales= 80_000_000,
                            deducciones_generales= 10_000_000,
                            aporte_pension= 6_400_000,
                            aporte_salud= 3_200_000,
                            numero_dependientes= 2,
                            tiene_vivienda_propia= True,
                            intereses_credito_vivienda= 5_000_000  )

        
 
        CalculadoraController.insertar( impuesto )
        
  
        impuesto_buscar = CalculadoraController.buscar_impuesto( impuesto.id )
        
  
        self.assertTrue(  impuesto.is_equal( impuesto_buscar )  )

    def testInsertAndSelect( self ):

   
        impuesto_prueba  = Calculadora( id= 2,ingresos_anuales= 180_000_000,
                            deducciones_generales= 18_000_000,
                            aporte_pension= 10_400_000,
                            aporte_salud= 9_200_000,
                            numero_dependientes= 0,
                            tiene_vivienda_propia= True,
                            intereses_credito_vivienda= 3_500_000  )
        CalculadoraController.insertar( impuesto_prueba )


        impuesto_buscado = CalculadoraController.buscar_impuesto( id=2 )
  
        impuesto_buscado.is_equal( impuesto_prueba )    
    def testPrimaryKey(self):

        impuesto_prueba  = Calculadora( id= 1,ingresos_anuales= 180_000_000,
                            deducciones_generales= 18_000_000,
                            aporte_pension= 10_400_000,
                            aporte_salud= 9_200_000,
                            numero_dependientes= 0,
                            tiene_vivienda_propia= True,
                            intereses_credito_vivienda= 3_500_000 )
        CalculadoraController.insertar( impuesto_prueba )


        impuesto_otro  = Calculadora( id= 1,ingresos_anuales= 180_000_000,
                            deducciones_generales= 18_000_000,
                            aporte_pension= 10_400_000,
                            aporte_salud= 9_200_000,
                            numero_dependientes= 0,
                            tiene_vivienda_propia= True,
                            intereses_credito_vivienda= 3_500_000 )
        
        self.assertRaises( Exception, CalculadoraController.insertar, impuesto_otro)

if __name__ == '__main__':
    unittest.main()        