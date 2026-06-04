
from flask import Flask, request, jsonify , url_for   

from flask import render_template

import sys
sys.path.append("src")


from view.web import vista_calculadora


app = Flask(__name__)     

 
app.register_blueprint( vista_calculadora.blueprint )


if __name__=='__main__':
   app.run( )