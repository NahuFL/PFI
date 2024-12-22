
import sqlite3
from MenuFunciones import *
from DbFunciones import *

#Función principal
def main():
    cierre = True

    #Creamos la tabla productos
    crearTablaProductos()
    #Ciclo del programa
    while cierre:

        # Menú y selector de opción
        opcion = menu()

        # Opción de alta de producto
        if opcion == 1:
            agregarProducto()

        # Opción para consultar datos de un producto
        elif opcion == 2:
            consultarProducto()
            
        # Opción para modificar stock de un producto
        elif opcion == 3:
            modificarProducto()
            
        # Opción para eliminar un producto del stock
        elif opcion == 4:
            eliminarProducto()

        # Opción para ver el listado de stock
        elif opcion == 5:
            mostrarInventario()

        # Opción de productos con stock bajo
        elif opcion == 6:
            verficarStock()  

        # Opción de salida del programa
        elif opcion == 7:
            print("\nHasta la próxima")
            cierre = False

        # En caso de opciones inválidas
        else:
            print("\n--Ingrese una opción válida--")
            print()

#Llamada a la función principal
main()