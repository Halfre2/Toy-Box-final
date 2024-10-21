import CRUD as conn
from Mantenimiento_productos1 import Productos
from procesoCompra import ProcesoCompra
from mantenimiento_categorias import Categorias
from mantenimiento_clientes import Usuarios
from mantenimiento_ventas import Ventas

# Se instancia la conexión a la base de datos utilizando la clase Database del módulo CRUD.
db = conn.Database()

# Clase principal del menú de inicio que controla la navegación inicial del sistema.
class MenuInicio:
    def __init__(self):
        pass

    # Método para mostrar el menú principal de opciones.
    def mostrar_menu_inicio(self):
        while True:
            print("\t===============================")
            print("Sistema de administración y ventas | Tienda de juguetes")
            print("\t===============================")
            print("[1] Proceso de compra")
            print("[2] Servicios administrativos")
            print("[3] Salir")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    # Si elige el proceso de compra, instancia el menú de proceso de compra.
                    proceso_compra = ProcesoCompra()
                    proceso_compra.mostrar_menu_proceso_compra()
                elif option == 2:
                    # Si elige servicios administrativos, instancia el menú de categorías.
                    menu_categorias = MenuCategorias()
                    menu_categorias.mostrar_menu_categorias()
                elif option == 3:
                    # Opción para salir del sistema.
                    print("Has elegido salir, hasta pronto!")
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

# Clase para mostrar el menú de opciones administrativas.
class MenuCategorias:
    def __init__(self):
        # Instancia de los módulos de productos, categorías, usuarios y ventas.
        self.productos = Productos()
        self.categorias = Categorias()
        self.usuarios = Usuarios()
        self.ventas = Ventas()

    # Menú para elegir la funcionalidad administrativa.
    def mostrar_menu_categorias(self):
        while True:
            print("\t===============================")
            print("Servicios administrativos | Categorías")
            print("\t===============================")
            print("[1] Mantenimiento de productos")
            print("[2] Mantenimiento de categorías")
            print("[3] Mantenimiento de ventas")
            print("[4] Mantenimiento de usuarios")
            print("[5] Volver al menú principal")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    # Opción para el mantenimiento de productos.
                    menu_productos = Menu()
                    menu_productos.mostrar_menu()
                elif option == 2:
                    # Opción para el mantenimiento de categorías.
                    self.mostrar_menu_categorias_mantenimiento()
                elif option == 3:
                    # Opción para el mantenimiento de ventas.
                    self.mostrar_menu_ventas_mantenimiento()
                elif option == 4:
                    # Opción para el mantenimiento de usuarios.
                    self.mostrar_menu_usuarios_mantenimiento()
                elif option == 5:
                    # Regresa al menú principal.
                    break
                else:
                    print("Esta funcionalidad aún no está implementada.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    # Menú de mantenimiento de categorías.
    def mostrar_menu_categorias_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de categorías")
            print("\t===============================")
            print("[1] Agregar Categoría")
            print("[2] Ver Categorías")
            print("[3] Modificar Categoría")
            print("[4] Eliminar Categoría")
            print("[5] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    # Agrega una categoría.
                    self.categorias.agregar_categoria()
                elif option == 2:
                    # Muestra las categorías existentes.
                    self.categorias.mostrar_categorias()
                elif option == 3:
                    # Modifica una categoría existente.
                    self.categorias.modificar_categoria()
                elif option == 4:
                    # Elimina una categoría.
                    self.categorias.eliminar_categoria()
                elif option == 5:
                    # Vuelve al menú anterior.
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    # Menú para mantenimiento de ventas.
    def mostrar_menu_ventas_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de ventas")
            print("\t===============================")
            print("[1] Cambiar Estado de Envío")
            print("[2] Buscar Venta")
            print("[3] Ver Detalle de Venta")
            print("[4] Eliminar Venta")
            print("[5] Ver Ventas")
            print("[6] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))

                if option == 1:
                    # Cambia el estado de envío de una venta.
                    self.ventas.cambiar_estado_envio()
                elif option == 2:
                    # Busca una venta específica.
                    self.ventas.buscar_venta()
                elif option == 3:
                    # Muestra el detalle de una venta.
                    self.ventas.ver_detalle_venta()
                elif option == 4:
                    # Elimina una venta.
                    self.ventas.eliminar_venta()
                elif option == 5:
                    # Muestra todas las ventas.
                    self.ventas.ver_ventas()
                elif option == 6:
                    # Regresa al menú anterior.
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    # Menú para mantenimiento de usuarios.
    def mostrar_menu_usuarios_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de usuarios")
            print("\t===============================")
            print("[1] Agregar Usuario")
            print("[2] Buscar Usuario")
            print("[3] Ver Usuarios")
            print("[4] Modificar Usuario")
            print("[5] Eliminar Usuario")
            print("[6] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    # Agrega un nuevo usuario.
                    self.usuarios.agregar_usuario()
                elif option == 2:
                    # Busca un usuario específico.
                    self.usuarios.buscar_usuario()
                elif option == 3:
                    # Muestra la lista de usuarios.
                    self.usuarios.ver_usuarios()
                elif option == 4:
                    # Modifica la información de un usuario.
                    self.usuarios.modificar_usuario()
                elif option == 5:
                    # Elimina un usuario.
                    self.usuarios.eliminar_usuario()
                elif option == 6:
                    # Vuelve al menú anterior.
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

# Clase para manejar el menú de productos.
class Menu:
    def __init__(self):
        self.productos = Productos()

    # Menú principal para productos.
    def mostrar_menu(self):
        while True:
            print("\t===============================")
            print("Tienda de juguetes")
            print("\t===============================")
            print("[1] Agregar Productos")
            print("[2] Ver Productos")
            print("[3] Modificar Productos")
            print("[4] Eliminar Productos")
            print("[5] Salir")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    # Agrega un nuevo producto.
                    self.productos.agregar_producto()
                elif option == 2:
                    # Muestra los productos disponibles.
                    self.productos.mostrar_productos()
                elif option == 3:
                    # Modifica la información de un producto.
                    self.productos.modificar_producto()
                elif option == 4:
                    # Elimina un producto.
                    self.productos.eliminar_producto()
                elif option == 5:
                    print("Has elegido salir, hasta pronto!")
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

# Punto de entrada principal del programa.
if __name__ == "__main__":
    menu_inicio = MenuInicio()
    menu_inicio.mostrar_menu_inicio()
