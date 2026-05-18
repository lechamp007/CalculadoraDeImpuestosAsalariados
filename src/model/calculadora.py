class Calculadora: 
    def __init__(self,id,ingresos_anuales,deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda ):
        self.id = id
        self.ingresos_anuales =ingresos_anuales
        self.deducciones_generales= deducciones_generales   
        self.aporte_pension= aporte_pension   
        self.aporte_salud= aporte_salud   
        self.numero_dependientes= numero_dependientes   
        self.tiene_vivienda_propia= tiene_vivienda_propia
        self.intereses_credito_vivienda=intereses_credito_vivienda

    def is_equal(self,otro) -> bool:
        assert( int(self.id) == int(otro.id) )
        assert( float(self.ingresos_anuales) == float(otro.ingresos_anuales) )
        assert( float(self.deducciones_generales) == float(otro.deducciones_generales))
        assert( float(self.aporte_pension) == float(otro.aporte_pension) )
        assert( float(self.aporte_salud) == float(otro.aporte_salud ) )
        assert( int(self.numero_dependientes) == int(otro.numero_dependientes))
        assert( bool(self.tiene_vivienda_propia) == bool(otro.tiene_vivienda_propia)  )
        assert( float(self.intereses_credito_vivienda) == float(otro.intereses_credito_vivienda) )
        return True 
        












