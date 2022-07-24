import cx_Oracle
from flask import Flask, jsonify, render_template, request, flash

app = Flask(__name__)
app.secret_key='bacc68609f8cffa2fdeb6676ed7433940f309f0f8c1f5992'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/estudiante')
def estudiantemodulo():
    return render_template('estudiante.html')

@app.route('/empleado')
def empleadomodulo():
    return render_template('empleado.html')

@app.route('/registrar_empleado', methods=('GET','POST'))
def registrar_empleado():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipoDocumento= request.form['tipoDocumento']
        numeroDocumento= request.form['numeroDocumento']
        telefono=request.form['telefono']
        correo=request.form['correo']
        cargo= request.form['cargo']
        codigoEmpleado=request.form['codigoEmpleado']
        dependencia=request.form['dependencia']
        fecha=request.form['fecha']
        if not nombres:
            flash('nombres is required!','alert')
        elif not apellidos:
            flash('apellidos is required!','alert')
        elif not tipoDocumento or tipoDocumento=="Tipo documento...":
            flash('tipoDocumento is required!','alert')
        elif not numeroDocumento:
            flash('numeroDocumento is required!','alert')
        elif not telefono:
            flash('telefono is required!','alert')
        elif not correo:
            flash('correo is required!','alert')
        elif not cargo or cargo=="Cargo...":
            flash('cargo is required!','alert')
        elif not codigoEmpleado:
            flash('codigoEmpleado is required!','alert')
        elif not dependencia:
            flash('dependencia is required!','alert')
        elif not fecha:
            flash('fecha is required!','alert')
        else:
            print(nombres,apellidos,tipoDocumento,numeroDocumento,telefono,correo,cargo,codigoEmpleado,dependencia,fecha)
            flash('empleado registrado','success')
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



@app.route('/modificar_empleado', methods=('GET','POST'))
def modificar_empleado():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipoDocumento= request.form['tipoDocumento']
        numeroDocumento= request.form['numeroDocumento']
        telefono=request.form['telefono']
        correo=request.form['correo']
        cargo= request.form['cargo']
        dependencia=request.form['dependencia']
        fecha=request.form['fecha']
        if not nombres:
            flash('nombres is required!','alert')
        elif not apellidos:
            flash('apellidos is required!','alert')
        elif not tipoDocumento or tipoDocumento=="Tipo documento...":
            flash('tipoDocumento is required!','alert')
        elif not numeroDocumento:
            flash('numeroDocumento is required!','alert')
        elif not telefono:
            flash('telefono is required!','alert')
        elif not correo:
            flash('correo is required!','alert')
        elif not cargo or cargo=="Cargo...":
            flash('cargo is required!','alert')
        elif not dependencia:
            flash('dependencia is required!','alert')
        elif not fecha:
            flash('fecha is required!','alert')
        else:
            print(nombres,apellidos,tipoDocumento,numeroDocumento,telefono,correo,cargo,dependencia,fecha)
            flash('empleado modificado','success')
        return render_template('modificar_empleado.html')
    elif request.method=='GET':
        codigo=request.args.get('codigo', default = '', type = str)
        if not codigo or codigo=='':
            return render_template('modificar_empleado.html')
        else:
            print(codigo)
            info={'nombres':'jorge','apellidos':'perez','tipoDocumento':'CC','numeroDocumento':'1014444'}
            return render_template('modificar_empleado.html',form=info)


if __name__=='__main__':
    app.run(debug=True, port=5017)
