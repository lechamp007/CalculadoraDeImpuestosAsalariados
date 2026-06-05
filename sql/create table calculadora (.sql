create table calculadora (
    id INTEGER PRIMARY KEY,
    ingresos_anuales FLOAT NOT NULL,
    deducciones_generales FLOAT NOT NULL,
    aporte_pension FLOAT NOT NULL,
    aporte_salud FLOAT NOT NULL,
    numero_dependientes INT NOT NULL,
    tiene_vivienda_propia BOOLEAN NOT NULL,
    intereses_credito_vivienda FLOAT NOT NULL
); 