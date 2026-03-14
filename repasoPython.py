import pandas as pd
from flask import Flask,request,jsonify

app = Flask(__name__)


datos =pd.read_excel("personas_colombia.xlsx")
print(datos)


datos = datos.dropna()
print(datos)
datos = datos.drop_duplicates()
print(datos)

@app.route("/juevesPersonas",methods=['GET'])
def obtenerDatos():
    return jsonify(datos.to_dict(orient='records'))

print(datos.describe())

tablaAgrupada = datos.groupby("Género")['Edad'].agg(['mean','count','std','max','min']).reset_index()
                                                     
print(tablaAgrupada)   


@app.route("/agrupacionjueves",methods=['GET'])
def obtenerAgrupacion():
    return jsonify(tablaAgrupada.to_dict(orient='records'))


if __name__=='__main__':
    app.run(debug=True)