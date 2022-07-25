from warnings import catch_warnings
import cx_Oracle
from flask import Flask, jsonify, render_template, request, flash

conexion = cx_Oracle.connect(
user='cdrodriguezl',
password='cdrodriguezl',
dsn='localhost/xe')

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
    cur_01=conexion.cursor()
    select_empleados= " select * from persona join empleado ON persona.idpersona = empleado.idpersonafk2 join empleado_cargo ON empleado.idempleado = empleado_cargo.idempleadofk"
    cur_01.execute(select_empleados)
    resultados=cur_01.fetchall()

    resultadosjson=[]
    for resultado in resultados: 
        resultadosjson.append({
            "nombre":resultado[2],
            "apellido":resultado[3],
            "tipodocumento":resultado[1],
            "numerodocumento":resultado[0],
            "idempleado":resultado[6],
            "dependencia":resultado[8],
            "cargo":resultado[10]
        })

    return render_template('empleado.html',resultados=resultadosjson)

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
        fecha=request.form['fecha'].replace('-','/')
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
            try:
                print(nombres,apellidos,tipoDocumento,numeroDocumento,telefono,correo,cargo,codigoEmpleado,dependencia,fecha)
                cur_01=conexion.cursor()
                insert_datos= "insert into persona (idpersona, nombre, apellido, telefono, correo, idtipodocumentofk) VALUES (:1, :2, :3, :4, :5, :6)"
                print(insert_datos)
                cur_01.execute(insert_datos,[numeroDocumento, nombres, apellidos, telefono, correo, tipoDocumento])
                insert_datos= "insert into empleado (idempleado, idpersonafk2, dependencia) VALUES (:1, :2, :3)"
                cur_01.execute(insert_datos,[codigoEmpleado, numeroDocumento, dependencia])
                insert_datos= "insert into empleado_cargo (idempleadofk, idcargofk, fechainicio) VALUES (:1, :2,TO_DATE(:3, 'yyyy/mm/dd'))"
                cur_01.execute(insert_datos,[codigoEmpleado, cargo, fecha])
                conexion.commit()
                flash('empleado registrado','success')
            except:
                flash('fallo','alert')

    return render_template('registrar_empleado.html')


@app.route('/modificar_empleado', methods=('GET','POST'))
def modificar_empleado():
    resultados=()
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
        
            cur_01=conexion.cursor()
            select_empleados= "  select * from persona join empleado ON persona.idpersona = empleado.idpersonafk2 join empleado_cargo ON empleado.idempleado = empleado_cargo.idempleadofk where empleado.idempleado = "+codigo
            cur_01.execute(select_empleados)
            resultados=cur_01.fetchone()


            return render_template('modificar_empleado.html',form=resultados)


if __name__=='__main__':
    app.run(debug=True, port=5017)
