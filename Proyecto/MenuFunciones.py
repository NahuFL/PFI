
from DbFunciones import *

#Función menu y selecto de opciones
def menu():
    #Ciclo para mostrar el menu
    while True:
        print("\n" + "*" * 30)
        print("Control De Stock")
        print("*" * 30)
        print("MENU")
        print("1. Alta de nuevo producto")
        print("2. Consulta datos de stock")
        print("3. Modificar stock de un producto")
        print("4. Baja de producto")
        print("5. Ver listado de todo el stock")
        print("6. Ver productos con bajo stock")
        print("7. Salir")
        print()
        #Validación de la opción seleccionada
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: #Si no es un número
            print("Por favor, ingrese un número válido.")
            continue
        return opcion

#Función para validar un número flotante positivo
def verificarPositivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0: #Si el valor no es positivo
                print("El valor debe ser mayor a 0.")
            else:
                return valor  # Retorna el valor si es válido
        except ValueError:
            print("Valor inválido, por favor ingrese un número.")

#Función para validar un número entero positivo
def verificarPositivoEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0: #Si el valor no es positivo
                print("El valor debe ser mayor a 0.")
            else:
                return valor  # Retorna el valor si es válido
        except ValueError:
            print("Valor inválido, por favor ingrese un número entero.")

#Función para añadir un producto a la base de datos
def agregarProducto():
    nombre = (input("Ingrese el nombre del producto ('salir' para terminar): ").capitalize()).strip()
    while not nombre: #Si el nombre está vacío
        nombre = (input("Ingrese el nombre del producto ('salir' para terminar): ").capitalize()).strip()
#Ciclo de ingreso continuo de productos
    while nombre != "Salir":  
        descripcion = input("Ingrese una breve descripción del producto: ")
        while not descripcion: #Si la descripción está vacía
            descripcion = input("Ingrese una breve descripción del producto: ").capitalize()
        cantidad = verificarPositivoEntero("Ingrese el stock del producto: ")
        precio = verificarPositivo("Ingrese el precio del producto: ")
        categoria = input("Ingrese la categoría del producto: ").capitalize()        
        insertarPoductoDb(nombre, descripcion, cantidad, precio, categoria) #Inserta el producto en la base de datos
        nombre = (input("Ingrese el nombre del siguiente producto ('salir' para terminar): ").capitalize()).strip()

#Funcion para consultar los datos de un producto
def consultarProducto():
    consultaProducto = verificarPositivoEntero("\nIngrese el 'id' del producto: ")
    stock = consultaProductoDb(consultaProducto) #Consulta el stock del producto en la base de datos
    if not stock:  #En caso de no encontrar el producto
        print("\nNo se encontro el producto en el inventario.\n")
    else: #Si se encuentra el producto, se imprimen sus datos
        print(f"* Producto: {stock[1]}")
        print(f"  - Descripción: {stock[2]}")
        print(f"  - Cantidad en stock: {stock[3]}")
        print(f"  - Precio unitario: ${stock[4]}")
        print(f"  - Categoría: {stock[5]}")
        print(f"  - ID: {stock[0]}\n")

#Función para modificar un producto
def modificarProducto(): 
    modificaProducto = verificarPositivoEntero("\nIngrese el 'id' del producto: ")
    stock = consultaProductoDb(modificaProducto) #Consulta el stock del producto en la base de datos
    if not stock: #En caso de no encontrar el producto
        print("No se encuentra stock del producto")
    else: #Si se encuentra el producto
        stock = list(stock) #Convierte el tupla en lista para poder modificarla.
        while True: #Ciclo para modificar el producto
            sumaRestaStock = input("Ingrese 'suma/resta' para agregar o quitar stock: ").lower()
            if sumaRestaStock != "suma" and sumaRestaStock != "resta": #Si la opción no es válida
                print("Ingreso erroneo, intente nuevamente.")
            else: #Si se ingresa una opción válida, rompe el ciclo
                break
        if sumaRestaStock == "suma": #Si la opción es suma, agrega el monto ingresado
            agregar = verificarPositivoEntero("Ingrese monto a agregar: ")
            stock[3] += agregar
            print()
        if sumaRestaStock == "resta": #Si la opción es resta, resta el monto ingresado
            quitar = verificarPositivoEntero("Ingrese monto a quitar: ")
            while quitar > stock[3]: #Si el monto a quitar es mayor que el stock
                print("Monto superior al stock disponible, vuelva a intentar: ")
                quitar = verificarPositivoEntero("Ingrese monto a quitar: ")
            stock[3] -= quitar
        modificarCantidadDb(stock[3], stock[0]) #Modifica el stock del producto en la base de datos
        consultaProductoDb(stock[0]) #Consulta el stock del producto en la base de datos
        if stock: #Si se encuentra el producto, se imprimen sus datos
            print(f"\n* Producto: {stock[1]}")
            print(f" - Descripción: {stock[2]}")
            print(f" - Cantidad en stock: {stock[3]}")
            print(f" - Precio: {stock[4]}")              
            print(f" - Categoría: {stock[5]}\n")                             

#Función para eliminar un producto
def eliminarProducto(): 
    productoId = verificarPositivoEntero("\nIngrese el 'id' del producto: ")
    producto = consultaProductoDb(productoId) #Consulta el stock del producto en la base de datos
    bajaProducto(producto) #Elimina el producto de la base de datos

#Función para mostrar el inventario
def mostrarInventario(): 
    stock = listadoDb() #Consulta el stock de todos los productos en la base de datos
    if not stock:  #En caso de inventario vacío
        print("\nNo hay productos en el inventario.")
    else: #Si hay productos en el inventario imprime los detalles
        for producto in stock:
            print(f"* Producto: {producto[1]}")
            print(f"  - Descripción: {producto[2]}")
            print(f"  - Cantidad en stock: {producto[3]}")
            print(f"  - Precio unitario: ${producto[4]}")
            print(f"  - Categoría: {producto[5]}")
            print(f"  - ID: {producto[0]}\n")

#Función para verificar el stock bajo del inventario
def verficarStock(): 
    cantidadMinima = verificarPositivo("Ingrese la cantidad minima de stock recomendado: ")
    stockBajo = bajoStockDb(cantidadMinima) #Consulta los productos con stock bajo en la base de datos
    if not stockBajo: #En caso de no encontrar productos con stock bajo
        print("\nNo hay productos con bajo stock")
    else: #Si hay productos con stock bajo imprime los detalles
        for producto in stockBajo:
            print(f"* Producto: {producto[1]}")
            print(f"  - Descripción: {producto[2]}")
            print(f"  - Cantidad en stock: {producto[3]}")
            print(f"  - Precio unitario: ${producto[4]}")
            print(f"  - Categoría: {producto[5]}")
            print(f"  - ID: {producto[0]}\n")
        