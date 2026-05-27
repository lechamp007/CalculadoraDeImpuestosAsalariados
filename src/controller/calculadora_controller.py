import sys
sys.path.append( "." )
sys.path.append( "src" )
import psycopg2
import secret_config
from model.calculadora import Calculadora

class CalculadoraController:

    def crear_tabla():
        cursor = CalculadoraController.obtener_cursor()
        with open("sql/crear-calculadora.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.connection.close()

    def borrar_tabla():
        cursor = CalculadoraController.obtener_cursor()
        with open("sql/borrar-calculadora.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.connection.close()

    def obtener_cursor():
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,          
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        cursor = connection.cursor()
        return cursor

    def insertar(calculadora: Calculadora):
        cursor = CalculadoraController.obtener_cursor()
        consulta = """
            INSERT INTO calculadora (
                id,
                ingresos_anuales,
                deducciones_generales,
                aporte_pension,
                aporte_salud,
                numero_dependientes,
                tiene_vivienda_propia,
                intereses_credito_vivienda
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            calculadora.id,
            calculadora.ingresos_anuales,
            calculadora.deducciones_generales,
            calculadora.aporte_pension,
            calculadora.aporte_salud,
            calculadora.numero_dependientes,
            calculadora.tiene_vivienda_propia,
            calculadora.intereses_credito_vivienda
        )
        cursor.execute(consulta, valores)
        cursor.connection.commit()
        cursor.connection.close()
        return calculador.id
    def buscar_impuesto(id):
        cursor = CalculadoraController.obtener_cursor()
        consulta = """
            SELECT
                id,
                ingresos_anuales,
                deducciones_generales,
                aporte_pension,
                aporte_salud,
                numero_dependientes,
                tiene_vivienda_propia,
                intereses_credito_vivienda
            FROM public.calculadora
            WHERE id = %s
        """
        cursor.execute(consulta, (id,))    
        resultado = cursor.fetchone()
        cursor.connection.close()

        if resultado is None:
            raise ValueError(f"No existe un registro con id={id}")

        calculadora = Calculadora(
            id                         = str(resultado[0]),
            ingresos_anuales           = resultado[1],
            deducciones_generales      = resultado[2],
            aporte_pension             = resultado[3],
            aporte_salud               = resultado[4],
            numero_dependientes        = resultado[5],
            tiene_vivienda_propia      = resultado[6],
            intereses_credito_vivienda = resultado[7]
        )
        return calculadora

    def eliminar_impuesto(id):
        cursor = CalculadoraController.obtener_cursor()
        consulta = "DELETE FROM public.calculadora WHERE id = %s"
        cursor.execute(consulta, (id,))    
        cursor.connection.commit()
        cursor.connection.close()