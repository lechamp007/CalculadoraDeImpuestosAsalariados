import sys
sys.path.append("src")
from flask import Flask
from flask import render_template, request
from model.logica_calculadora_impuestos import CalcularImpuesto, VariablesImpuestos

app = Flask(__name__)

@app.route('/home_impuesto')
def home_impuesto():
    return render_template("home_impuesto.html")

@app.route('/calcular_impuesto')
def calcular_impuesto():
    impuesto= VariablesImpuestos(ingresos_anuales= float(request.args["ingresos_anuales"]), deducciones= float(request.args["deducciones"]),
                                 pension=float(request.args["pension"]), salud=float(request.args["salud"]),
                                 dependientes=int(request.args["dependientes"]), tiene_vivienda_propia=bool(request.args["vivienda_propia"]),
                                 intereses_vivienda=float(request.args["interes_credito"]))
    resultado_impuesto= CalcularImpuesto.calcular_impuesto_renta(impuesto)
    return render_template("impuesto_resultado.html", resultado_impuesto= resultado_impuesto)


if __name__=='__main__':
    app.run(debug=True)
                               