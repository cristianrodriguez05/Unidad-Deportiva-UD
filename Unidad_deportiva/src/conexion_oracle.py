from ast import Str
import cx_Oracle

try:
    conexion = cx_Oracle.connect(
    user='cdrodriguezl',
    password='cdrodriguezl',
    dsn='localhost/xe')
except Exception as err:
    print('error', err)
    
else:
    print('Establecida', conexion.version)

try:
    cur_01=conexion.cursor()
    insert_datos= '''insert into tipoDocumento values(
        'CCC' , 'cedula')'''
    cur_01.execute(insert_datos)
except Exception as err:
    print('error', err)
    
else:
    print('Insertados')
    conexion.commit()


conexion.close()
