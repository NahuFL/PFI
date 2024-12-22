
import sqlite3

def crearTablaProductos(): #Función para crear la tabla de productos
    try:   
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    cantidad INTERGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT)''')
        conexion.commit()
    except sqlite3.Error as error:
        print(f"Error al crear la tabla: ", {error})
    finally:
        if conexion:
            conexion.close()

def consultaProductoDb(id): #Función para consultar un producto en la base de datos, con informe de error.
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        query = "SELECT * FROM productos WHERE id = ?"
        placeholder = (id,)
        cursor.execute(query, placeholder)
        stock = cursor.fetchone()
        return stock
    except sqlite3.Error as error: #Si hay un error, se imprime
        print(f"Error al consultar el producto: {error}")
        return None
    finally: #Siempre se cierra la conexión.
        if conexion:
            conexion.close()

def insertarPoductoDb(nombre, descripcion, cantidad, precio, categoria): #Función para insertar un producto en la base de datos, con informe de error.
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                        VALUES (?, ?, ?, ?, ?)''',
                        (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print(f"\nProducto '{nombre}' agregado al inventario\n")
    except sqlite3.Error as error: #Si hay un error, se imprime
        print(f"\nError al agregar producto '{nombre}': {error}\n")
    finally: #Siempre se cierra la conexión.
        if conexion:
            conexion.close()

def bajaProducto(producto): #Función para eliminar un producto de la base de datos, con informe de error.
    if producto: #Si el producto existe
        try:
            conexion = sqlite3.connect("inventario.db")
            cursor = conexion.cursor()
            query = "DELETE FROM productos WHERE id = ?"
            placeholder = (producto[0],)
            cursor.execute(query, placeholder)
            conexion.commit()
            print("\nProducto eliminado exitosamente")
        except Exception as error: #Si hay un error, se imprime
            print(f"\nError al eliminar el producto: {error}")
        finally: #Siempre se cierra la conexión.
            conexion.close()
    else: #Si el producto no existe
        print("\nNo se encontro el producto")

def listadoDb(): #Función para traer el listado de productos en la base de datos, con informe de error.
    print("\n" + "*" * 30 + "Listado del stock total" + "*" * 30)
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query,)
        stock = cursor.fetchall()
    except sqlite3.Error as error: #Si hay un error, se imprime
        print(f"Error al consultar el inventario: {error}")
    finally: #Siempre se cierra la conexión.
        if conexion:
            conexion.close()
    return stock
    

def bajoStockDb(valor): #Función para traer los productos con stock bajo en la base de datos, con informe de error.
    try:
        print("\nListado de productos con bajo stock: ")
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        query = "SELECT * FROM productos WHERE cantidad < ?"
        placeholder = (valor,)
        cursor.execute(query, placeholder)
        productosStockBajo = cursor.fetchall()      
    except sqlite3.Error as error: #Si hay un error, se imprime
        print(f"\nError al obtener productos con bajo stock: {error}")
    finally: #Siempre se cierra la conexión.
        if conexion:
            conexion.close()
    return productosStockBajo

def modificarCantidadDb(cantidad, id ): #Función para modificar la cantidad de un producto en la base de datos, con informe de error
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        query = "UPDATE productos SET cantidad = ? WHERE id = ?"
        placeholder = (cantidad, id,)
        cursor.execute(query, placeholder)
        conexion.commit()
    except sqlite3.Error as error: #Si hay un error, se imprime
        print(f"\nError al modificar la cantidad del producto: {error}")
    finally: #Siempre se cierra la conexión.
        if conexion:
            conexion.close()

