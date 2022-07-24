from flask import Flask, render_template

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

@app.route('/modificar_empleado')
def modificar_empleado():
    return render_template('modificar_empleado.html')

if __name__=='__main__':
    app.run(debug=True, port=5017)
