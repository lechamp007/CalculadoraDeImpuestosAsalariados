import sys
sys.path.append( "." )
sys.path.append( "src" )
import secret_config
import psycopg2
import datetime

class CalculadoraController: 
    def obtener_cursor( ):
        #Conectar a la BD 
        connection = psycopg2.connect( database=secret_config.PGDATABASE, user=secret_config.PGHOST, password=secret_config.PGPASSWORD, host=secret_config.PGPORT)
        #Crear un objeto cursor 
        cursor = connection.cursor()
        return cursor
    def insertar(calculador: Calculadora):
        cursor= CalculadoraController.obtener_cursor()
        #Armar la instruccion SQL 
        consulta="""INSERT INTO calculadora(id,ingresos_anuales,deducciones_generales,
                    aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda) """
        #Ejecutar el SQL 
        cursor.execute(consulta)
        #Invoque a commit siempre que use una instruccion que modifica en la base de datos
        cursor.connection.commit()
    def buscar(id): 
        cursor =CalculadoraController.obtener_cursor()
        consulta="""SELECTid,ingresos_anuales,deducciones_generales,aporte_pension,aporte_salud,
                    numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda """
    