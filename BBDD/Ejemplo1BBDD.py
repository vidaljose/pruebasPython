import sqlite3

#TODO: pasos para utilizar bases de datos
#Abrir-crear conexion
#Ejecutar query(consulta) SQL
#Manejar el resultado de las query
#Cerrar puntero
#Cerrar conexion

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo varchar(50), precio integer, seccion varchar(20))")  #creando la base de datos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
#variosProductos=[
#    ("Camiseta",10,"Deportes"),
#    ("Jarron",90,"Ceramica"),
#    ("Camion",20,"Jugueteria")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
for i in variosProductos:
    print("Nombre Articulo: ", i[0], "Seccion: ",i[2])

miConexion.commit()

miConexion.close()