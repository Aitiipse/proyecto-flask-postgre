from flask import Flask, render_template, url_for , flash, request, redirect, session
from psycopg2 import connect
from config import *
app = Flask(__name__)

app.secret_key='12345'

con_db = EstablecerConexion()

#ruta de la pagina principal
@app.route("/")
def index():
    cur=con_db.cursor()
    sql= "SELECT*FROM personas"
    cur.execute(sql)
    PersonasRegistradas=cur.fetchall()
    return render_template('index.html',personas=PersonasRegistradas)
	

#ruta de layaut
@app.route("/layaut")
def layaut():
	print("Hola layut")
	return render_template("layout.html")

@app.route("/guardar_persona", methods=['POST'])
def guardar_personas():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		edad = request.form['edad']
		create_table()
		cur = con_db.cursor()
		cur.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)", (nombre, apellido, edad))
		con_db.commit()
		flash("registro guardado correctamente")
		return redirect(url_for('index'))

@app.route('/eliminar_persona/<int:id_persona>')
def eliminar(id_persona):
    cursor=con_db.cursor()
    sql="DELETE FROM personas WHERE id ={0}".format(id_persona)
    cursor.execute(sql)
    con_db.commit()
    return redirect(url_for('index'))
    
@app.route('/editar_persona/<int:id_persona>', methods=['POST'])
def editar(id_persona):
    cur = con_db.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    if nombre and apellido and edad:
        sql="UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
        cur.execute(sql,(nombre,apellido,edad,id_persona))
        con_db.commit()
        return redirect(url_for('index'))
    else:
    	return "error en la consulta" 
    
    
@app.route("/listar_personas")
def listar_personas():
	cur = con_db.cursor()
	cur.execute("SELECT * FROM personas")
	data = cur.fetchall()
	print(data)
	return render_template("ver.html", personas=data)

#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404

# funciones
def create_table():
	cur = con_db.cursor()
	cur.execute("""
			CREATE TABLE IF NOT EXISTS personas(
				id serial  NOT NULL,
				nombre VARCHAR(50),
				apellido VARCHAR(50),
				edad INTEGER,
				CONSTRAINT pk_personas_id PRIMARY KEY (id));
		""")
	con_db.commit()

if __name__ == '__main__':
	app.run(debug=True, port=5000)