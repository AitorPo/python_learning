import sqlite3

# Abrir conexion
conexion = sqlite3.connect('pruebas.db')

# Crear cursor => nos permite ejecutar la consukta
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255),
        descripcion TEXT,
        precio INT
    );
""")
# Guardar cambios
conexion.commit()

# Insertar datos
# cursor.execute("INSERT INTO productos VALUES(null, 'Producto1', 'Producto de prueba 1', 20)")

# conexion.commit()

# Borrar registros
"""
ESTO BORRA TODOS LOS REGISTIOS DE LA TABLA. FUNCIONA COMO UN TRUNCATE DE MYSQL
cursor.execute("DELETE FROM productos")
conexion.commit()
"""
# Insertar muchos registros de golpe
productos = [
    ('PC', 'Buen PC', 700),
    ('Móvil', 'Buen Móvil', 200),
    ('Placa base', 'Buena placa', 100),
    ('Tablet', 'Buena tablet', 900),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 100" )

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 500")
productos = cursor.fetchall()

for producto in productos:
    print(f'ID: {producto[0]}')
    print(f'Título: {producto[1]}')
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")
    
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone() 

print(producto)

# print(productos)
# Cerrar conexion
conexion.close()