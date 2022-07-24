import cx_Oracle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/estudiante')
def estudiantemodulo():
    return render_template('estudiante.html')

@app.route('/empleado')
def empleadomodulo():
    return render_template('empleado.html')

@app.route('/registrar_empleado')
def registrar_empleado():
    return render_template('registrar_empleado.html')
def registrar():
        tipodoc = request.form('inputTipodocumento')
        numerodoc = request.form('inputNumerodocumento')
        try:
            conexion = cx_Oracle.connect(
            user='cdrodriguezl',
            password='cdrodriguezl',
            dsn='localhost/xe')
        except Exception as err:
            print('error')

        try:
            cur_01=conexion.cursor()
            insert_datos= '''insert into tipoDocumento values(
            tipodoc , numerodoc)'''
            cur_01.execute(insert_datos)
        except Exception as err:
            print('error', err)
    
        else:
            print('Insertados')
        conexion.commit()



@app.route('/modificar_empleado')
def modificar_empleado():
    return render_template('modificar_empleado.html')



if __name__=='__main__':
    app.run(debug=True, port=5017)
