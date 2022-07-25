from ast import Try
from turtle import update
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
            "cargo":resultado[11]
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
    resultadosjson={
                    "Nombre":"nombres",
                    "Apellidos":"apellidos",
                    "Telefono":"telefono",
                    "Correo":"correo",
                    "Cargo":"cargo",
                    "Dependencia":"dependencia",
                    "Codigo":1,
                    "Documento":1,
                    "IdEmpleadoCargo":1            
                    }
    if request.method == 'POST':
        codigo=request.args.get('codigo', default = '', type = str)
        documento=request.args.get('documento', default = '', type = str)
        idempleadocargo=request.args.get('idempleadocargo', default = '', type = str)
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono=request.form['telefono']
        correo=request.form['correo']
        cargo= request.form['cargo']
        dependencia=request.form['dependencia']
        fecha=request.form['fecha'].replace('-','/')

        update_persona='UPDATE persona set '
        update_persona_bool=False
        update_persona_atributos=[]
        update_empleado='UPDATE empleado set '
        update_empleado_bool=False
        update_empleado_atributos=[]
        update_empleado_cargo='UPDATE empleado_cargo set  '
        update_empleado_cargo_bool=False
        update_empleado_cargo_atributos=[]
        if (not codigo or codigo=='') and (not documento or documento=='') and (not idempleadocargo or idempleadocargo==''):
            flash('Error al actualizar','alert')
        else:
            if nombres and nombres!='':
                update_persona_bool=True
                update_persona_atributos.append("nombre='"+nombres+"'")
            if apellidos and apellidos!='':
                update_persona_bool=True
                update_persona_atributos.append("apellido='"+apellidos+"'")
            if telefono and telefono!='':
                update_persona_bool=True
                update_persona_atributos.append("telefono='"+telefono+"'")
            if correo and correo!='':
                update_persona_bool=True
                update_persona_atributos.append("correo='"+correo+"'")
            if cargo and cargo!="Cargo...":
                update_empleado_cargo_bool=True
                update_empleado_cargo_atributos.append("idcargofk='"+cargo+"'")
            if dependencia and dependencia!='':
                update_empleado_bool=False
                update_empleado_atributos.append("dependencia='"+dependencia+"'")
            if fecha and fecha!='':
                update_empleado_cargo_bool=True
                update_empleado_cargo_atributos.append("fechainicio=TO_DATE('"+fecha+"', 'yyyy/mm/dd')")

            cur_01=conexion.cursor()
            if update_persona_bool:
                try:
                    update_persona=update_persona+','.join(update_persona_atributos)+" Where idpersona = "+documento
                    print(update_persona)
                    cur_01.execute(update_persona)
                    conexion.commit()
                except:
                    flash('fallo al actualizar','alert')
            if update_empleado_bool:
                try:
                    update_empleado=update_empleado+','.join(update_empleado_atributos)+' where idempleado ='+codigo
                    print(update_empleado)
                    cur_01.execute(update_empleado)
                except:
                    flash('fallo al actualizar','alert')
            if update_empleado_cargo_bool:
                try:
                    update_empleado_cargo=update_empleado_cargo+','.join(update_empleado_cargo_atributos)+' where idempleado_cargo ='+idempleadocargo
                    print(update_empleado_cargo)
                    cur_01.execute(update_empleado_cargo)

                except:
                    flash('fallo al actualizar','alert')
    
            flash('empleado modificado','success')
            return render_template('modificar_empleado.html',form=resultadosjson)
    elif request.method=='GET':
        codigo=request.args.get('codigo', default = '', type = str)
        if not codigo or codigo=='':
            return render_template('modificar_empleado.html',form=resultadosjson)
        else:
            cur_01=conexion.cursor()
            select_empleados= "  select * from persona join empleado ON persona.idpersona = empleado.idpersonafk2 join empleado_cargo ON empleado.idempleado = empleado_cargo.idempleadofk where empleado.idempleado = "+codigo
            cur_01.execute(select_empleados)
            resultados=cur_01.fetchone()
            print(resultados)
            if resultados:
                resultadosjson={
                    "Nombre":resultados[2],
                    "Apellidos":resultados[3],
                    "Telefono":resultados[5],
                    "Correo":resultados[4],
                    "Cargo":resultados[11],
                    "Dependencia":resultados[8],
                    "Codigo":resultados[6],
                    "Documento":resultados[0],
                    "IdEmpleadoCargo":resultados[9]
                }
            else:
                flash("Empleado no encontrado","alert")
            return render_template('modificar_empleado.html',form=resultadosjson)


if __name__=='__main__':
    app.run(debug=True, port=5017)
