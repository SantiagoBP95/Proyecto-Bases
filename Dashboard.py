from dash import Dash, html, dcc
import plotly.express as px
import psycopg2

cursor = None
connection = None
try:
    connection = psycopg2.connect(host = 'localhost', user = 'postgres',
                                  password = '123456789', database = 'Proyecto',
                                  port = 5433)

    cursor = connection.cursor()
    cursor.execute("select departamento, count(departamento) from usuario JOIN suscripcion ON suscripcion.cedula = usuario.cedula group by(departamento);")
    rows = cursor.fetchall()
    cursor.execute("select published_date, count(published_date) from curso group by(published_date) order by published_date asc;")
    rows1 = cursor.fetchall()
    cursor.execute("select num_lectures, num_suscribers from curso order by num_lectures;")
    rows2 = cursor.fetchall()
    cursor.execute("select materia.nombre, count(materia.nombre) from curso join materia on materia.codigo = curso.codigo_materia group by(nombre);")
    rows3 = cursor.fetchall()
    cursor.execute("select materia.nombre, avg(price) from curso join materia on materia.codigo = curso.codigo_materia group by(nombre);")
    rows4 = cursor.fetchall()
    cursor.execute("select tipo, count(tipo) from curso join nivel on nivel.codigo = curso.codigo_nivel group by (tipo);")
    rows5 = cursor.fetchall()
    cursor.execute("select tipo, count(tipo) from curso join forma_de_pago on forma_de_pago.codigo_pago = curso.codigo_forma_pago group by (tipo);")
    rows6 = cursor.fetchall()
    cursor.execute("select nivel.tipo, avg(price) from curso join nivel on nivel.codigo = curso.codigo_nivel group by(tipo);")
    rows7 = cursor.fetchall()
    cursor.execute("select ciudad, count(ciudad) from usuario JOIN suscripcion ON suscripcion.cedula = usuario.cedula group by(ciudad);")
    rows8 = cursor.fetchall()
    cursor.execute("select materia.nombre, sum(num_lectures) from curso join materia on materia.codigo = curso.codigo_materia group by(materia.nombre); ")
    rows9 = cursor.fetchall()
    cursor.execute("select materia.nombre, sum(num_suscribers) from curso join materia on materia.codigo = curso.codigo_materia group by(materia.nombre); ")
    rows10 = cursor.fetchall()
    
    app = Dash(__name__)
    fig = px.bar(rows, x = 0, y = 1, color_discrete_sequence = ["#1c3166"])
    fig8 = px.bar(rows8, x = 0, y = 1, color_discrete_sequence = ["#1c3166"])
    fig1 = px.line(rows1, x = 0, y = 1, color_discrete_sequence = ["#00ffff"])
    fig2 = px.line(rows2, x = 0, y = 1, color_discrete_sequence = ["#1c4442"])
    fig9 = px.bar(rows9, x = 0, y = 1, color_discrete_sequence = ["#1c4442"])
    fig10 = px.bar(rows10, x = 0, y = 1, color_discrete_sequence = ["#1c4442"])
    fig3 = px.pie(rows3, names = 0, values= 1, color_discrete_sequence = ["#1c4442"])
    fig4 = px.bar(rows4, x = 0, y = 1, color_discrete_sequence = ["#1c4442"])
    fig5 = px.pie(rows5, names = 0, values = 1, color_discrete_sequence = ["#ffd966"])
    fig7 = px.bar(rows7, x = 0, y = 1, color_discrete_sequence = ["#ffd966"])
    fig6 = px.bar(rows6, x = 0, y = 1, color_discrete_sequence = ["#c348ff"])
    
    app.layout = html.Div(children=[
        html.H1(children = "Departamento, Suscripciones"),
        dcc.Graph(id = 'Departamento vs Suscripciones', figure = fig), 
        html.H1(children = "Ciudad, Suscripciones"),
        dcc.Graph(id = 'Ciudad vs Suscripciones', figure = fig8), 
        html.H1(children = "Fecha de publicaci??n, N??mero de cursos"),
        dcc.Graph(id = 'Fecha de publicaci??n vs N??mero de cursos', figure = fig1), 
        html.H1(children = "Numero de lecturas, Suscripciones"),
        dcc.Graph(id = 'Numero de lecturas vs Suscripciones', figure = fig2),
        html.H1(children = "Materia, N??mero de lecturas"),
        dcc.Graph(id = 'Materia vs N??mero de lecturas', figure = fig9),
        html.H1(children = "Materia, N??mero de suscripciones"),
        dcc.Graph(id = 'Materia vs N??mero de suscripciones', figure = fig10),
        html.H1(children = "Materia, N??mero de cursos"),
        dcc.Graph(id = 'Materia vs N??mero de cursos', figure = fig3),
        html.H1(children = "Materia, Precio promedio"),
        dcc.Graph(id = 'Materia vs Precio promedio', figure = fig4),
        html.H1(children = "Nivel, N??mero de cursos"),
        dcc.Graph(id = 'Nivel vs N??mero de cursos', figure = fig5),
        html.H1(children = "Nivel, Precio promedio"),
        dcc.Graph(id = 'Nivel vs N??mero de cursos', figure = fig7),
        html.H1(children = "Cursos de pago vs cursos gratuitos"),
        dcc.Graph(id = 'Cursos', figure = fig6),
        html.Br(),
        html.Div(id = 'Foro', children=[
            html.H1(children = 'Foro de preguntas'),
            html.H2(children ='??Como se organiza la cantidad de cursos tomados con respecto a las ciudades del pa??s?. ??Es la misma organizaci??n por departamentos?'),
            html.Br(),
            html.Div(children = '''Con este an??lisis se quiere comparar el n??mero de cursos tomados por cada ciudad y  as?? poder sacar alguna conclusi??n, del mismo modo se busca hacer eso con los departamentos y as?? tal vez comparar estas dos graficas y corroborar si existe una relaci??n entre las ciudades y sus departamentos. Para esto se va a usar un histograma: 
                     '''),
            html.Br(),
            html.Div(children = '''Julieta: Al hacer la comparaci??n entre las dos graficas, nos podemos dar cuenta que su relaci??n no es lineal. Porque siendo Antioquia el departamento con ma subscripciones, las ciudades con m??s cursos tomados no pertenecen a este departamento. Pertenecen al Tolima y a norte de Santander'''),
            html.Br(),
            html.Div(children = '''Sergio: Para comprobar linealidad, es m??s ??til a trav??s de una gr??fica de funci??n en plano ortogonal, teniendo como variable independiente la antig??edad del curso(x) y su n??mero de suscripciones como la variable dependiente (y) y visualmente discernir si es o no lineal.'''),
                     
            html.H2(children = '??C??mo se relaciona la fecha de publicaci??n con la cantidad de cursos publicados? Adem??s, ??La relaci??n entre la antig??edad del curso y su numero de suscripciones es lineal?'),
            html.Br(),
            html.Div(children = 'Con este an??lisis se busca interpretar el impacto del tiempo en el n??mero de cursos publicados.'),
            html.Br(),
            html.Div(children = 'Santiago: Como se puede evidenciar en la gr??fica de linea: fecha de publicaci??n vs N??mero de cursos publicados no existe un correlaci??n lineal directa entre estas variables. Sin embargo si es posible identificar que a medida que pasa el tiempo hay una mayor variabilidad en los datos con d??as en los que se llegan a publicar hasta 20 cursos. Por lo que en promedio considero que si hubo un aumento en la publicaci??n a lo largo del tiempo.'),
            html.Br(),
            html.Div(children = 'Julieta: Estoy de acuerdo con Santiago, aunque no hay una relaci??n lineal entre la fecha de publicaci??n y la cantidad de cursos. Por la grafica podemos notar que si existe una relaci??n entre ellos que no es directa ni inversa'),
            html.Br(),
            html.H2(children = '??C??mo se distribuye el n??mero de suscripciones por materia?, ??Es desigual?, ??Qu?? podemos decir del n??mero de lecturas por materia, se comporta de la misma manera?'),
            html.Br(),
            html.Div(children = 'Julieta: Al principio podr??amos decir que la relaci??n entre lecturas y suscriptores es lineal al ver su relaci??n con la materia, ya que tanto en el n??mero de suscriptores y el n??mero de lectura el mayor es el de desarrollo web. Sin embargo al ver la grafica de n??mero de suscriptores con el n??mero de lecturas, nos damos cuenta que esta relaci??n no es lineal.'),
            html.Br(),
            html.Div(children = 'Santiago: Considero que la proporci??n de suscripciones por materia es considerablemente mayor para los cursos de desarrollo web, alcanzando 75 visualizaciones y 42 suscripciones. En comparaci??n, los cursos de desarrollo web conforman el 32.7% de los regitros seguidos por los cursos de gesti??n empresarial con una proporci??n del 32.4%. Pienso que la preferencia por estas dos materias soporta tambi??n el mayor costo promedio de este grupo de cursos'),
            html.Br(),
            html.H2(children = '??Hay alguna relaci??n entre el nivel del curso y su precio?, ??C??mo se distribuye el n??mero de cursos por niveles? ??Podemos  otra vez decir algo al respecto de esas dos tablas?'),
            html.Br(),
            html.Div(children = 'Sergio: Podemos ver que el nivel con m??s cursos es el de "todos los niveles", seguido por principiante. As?? mismo el nivel con el promedio m??s alto es el de "todos los niveles", pero esta vez seguido por nivel intermedio. En ambos el nivel experto es tanto el que tiene menos cursos, como el que tiene el menor promedio de costo. Esto se puede interpretar f??cilmente ya que tiene sentido de que los cursos con niveles sin prerrequisitos ("todos los niveles" y "principiante") abunden para promocionarse m??s.'),
            html.Br(),
            html.Div(children = 'Santiago: En cuanto al precio, me doy cuenta que el nivel experto tiene un precio medio en torno a 8 d??lares menor lo cual me parece extra??o y tal vez se deba a que este grupo de cursos es de los cuales hay menos publicados. Por otro lado, los cursos dise??ados para todo el p??blico son con diferencia el nivel que m??s registros tiene en la base de datos.'),
            html.Br(),
            ]),
            html.Br(),
        html.Div(id = 'Conclusiones', children = [
            html.H1(children = 'Conclusiones'),
            html.Div(children = 'Sergio: Carga de datos: hubo problemas en un principio al exportar los datos desde las tablas normalizadas hasta la base de datos en postgres, al ser una carga de datos de un csv tan masivo donde no hay certeza de que todo archivo est?? bien. Toc?? manualmente a prueba y error encontrar errores del archivo csv(l??neas repetidas, desaparici??n de s??mbolos como la puntuaci??n, par??ntesis, l??neas corruptas etc.). Dificultaron este proceso. Y a cada vez ir a buscar esos errores entre los m??s de 3000 datos. Dise??o de la base de datos: No hubo problemas t??cnicos en cuanto a eso pero se debati?? varias veces como ser??a el modelo de este, incluso desde los mapas iniciales. Generar nuevas tablas para que sean m??s f??ciles de analizar o borrar tablas y columnas que resultaban innecesario para el objetivo a estudiar.'),
            html.Br(),
            html.Div(children = 'Julieta: Normalizaci??n: Al principio no estaba tan complicado, s??lo se separaron los datos, hasta volverlo at??micos, luego en la segunda forma normal, si fue m??s complicado porque nos dimos cuenta que nos hac??an falta crear entidades que no estaban y cambiar algunos datos. Luego para la tercera forma normal luego de crear la entidad de usuario que no estaba y definir bien las entidades. Lo m??s complicado fue hacer la entidad de suscripci??n ya que el llenado tuvo que ser manual, y para poder analizar bien los datos hab??a que poner varios usuarios en un solo curso'),
            html.Br(),
            html.Div('Santiago: Para el desarrollo del proyecto, en primer lugar, tuve la tarea de encontrar la base de datos. Usamos el repositorio de Kaggle porque particularmente ten??a inter??s en los cursos de Udemy y las categror??as de estos. En segundo lugar desarroll?? la conexi??n entre los lenguajes Python y postgres para poder graficar. No hubo problemas en la conexi??n, sin embargo, al momento de ordenar el dashboard fu?? necesario aprender el lenguaje HTML y su implementaci??n en la librer??a de Dash. A la hora de graficar e interpretar la informaci??n usamos una variedad amplia de graficas buscando unavisualizaci??n descriptiva de los datos. Finalmente, creo que las graficas y la base de datos responden a las preguntas planteadas y se ha culminado correctamente el proyecto.'),
            ])
        ])
    
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()