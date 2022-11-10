from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(host = 'localhost', user = 'postgres',
                                  password = '123456789', database = 'Proyecto',
                                  port = 5433)
    print('Conexión exitosa')
    cursor = connection.cursor()
    cursor.execute('select * from materia;')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print('Conexión finalizada')
    