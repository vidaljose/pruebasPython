import sqlite3

miConexio = sqlite3.connect("GestionProductos.db")

miCursor = miConexio.cursor()
# triple comilla para porder escribir en varias lineas // UNIQUE QUE NO SE REPITA LA INFORMACION
"""miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')


productos = [
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarron",45,"ceramica"),
    ("pantalones",15,"confeccion")
]
miCursor.executemany("INSERT INTO PRODUCTOS(NOMBRE_ARTICULO,PRECIO,SECCION) VALUES(?,?,?)", productos)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'JUGUETERIA')")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion' ")
productos =  miCursor.fetchall()
print("Los productos de tipo confeccion son: ")
for producto in productos:
    print(producto)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota' ") """
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")


miConexio.commit()
miConexio.close()
