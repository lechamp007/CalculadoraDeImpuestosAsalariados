import sys
sys.path.append( "." )
sys.path.append( "src" )
import secret_config
import psycopg2
import datetime

class CacluladoraController: 
    def obtener_cursor( ):
        #Conectar a la BD 
        connection = psycopg2.connect( database=secret_config.PGDATABASE, user=secret_config.PGHOST, password=secret_config.PGPASSWORD, host=secret_config.PGPORT)
        #Crear un objeto cursor 
        cursor = connection.cursor()
        return cursor
    def insertar(calculador: Calculadora):
        cursor= CacluladoraController.obtener_cursor()
        #Armar la instruccion SQL 
        consulta="""INSERT INTO calculadora """
        #Ejecutar el SQL 
        cursor.execute(consulta)
        #Invoque a commit siempre que use una instruccion que modifica en la base de datos
        cursor.connection.commit()
    def buscar 
    