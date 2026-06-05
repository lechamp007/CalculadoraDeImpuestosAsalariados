import sys
sys.path.append("src")
from flask import Blueprint
from flask import Flask
from flask import render_template, request
from model.logica_calculadora_impuestos import CalcularImpuesto, VariablesImpuestos
from controller.calculadora_controller import CalculadoraController

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

@blueprint.route('/')
def home_impuesto():
    return render_template("home_impuesto.html")
@blueprint.route('/crear_tabla')
def crear_tabla():
    CalculadoraController.borrar_tabla()
    CalculadoraController.crear_tabla()
    return render_template("tabla_creada.html")
@blueprint.route('/calcular_impuesto')
def calcular_impuesto():
    impuesto= VariablesImpuestos(id=int(request.args["cedula"]),ingresos_anuales= float(request.args["ingresos_anuales"]), deducciones= float(request.args["deducciones"]),
                                 pension=float(request.args["pension"]), salud=float(request.args["salud"]),
                                 dependientes=int(request.args["dependientes"]), tiene_vivienda_propia=bool(request.args["vivienda_propia"]),
                                 intereses_vivienda=float(request.args["interes_credito"]))
    resultado_impuesto= CalcularImpuesto.calcular_impuesto_renta(impuesto)
    CalculadoraController.insertar( impuesto )
    return render_template("impuesto_resultado.html", resultado_impuesto= resultado_impuesto)

@blueprint.route("/buscar_impuesto")
def buscar_usuario():
   id = request.args["id"]
   impuesto = CalculadoraController.buscar_impuesto(id)
   return render_template("buscar_impuesto.html", impuesto_buscado = impuesto )


if __name__=='__main__':
    blueprint.run(debug=True)