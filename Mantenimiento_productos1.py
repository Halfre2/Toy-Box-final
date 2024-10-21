# Importamos el módulo CRUD para la conexión y ejecución de consultas con la base de datos.
import CRUD as conn
# Instanciamos la conexión a la base de datos.
db = conn.Database()

# Clase que maneja todas las operaciones relacionadas con los productos en la tienda.
class Productos:
    def __init__(self):
        pass  # Constructor vacío ya que no necesitamos inicializar ningún valor por el momento.

    # Método que muestra una lista de categorías predefinidas.
    def mostrar_categorias(self):
        # Imprimimos las categorías predefinidas que el usuario puede seleccionar.
        print("""
        Categorías disponibles:
        1 - Vehículos de Juguete
        2 - Muñecas y Figuras de Acción
        3 - Juegos educativos
        4 - Electrónica para Niños
        5 - Deportes y Aire Libre
        6 - Peluches y Cojines
        7 - Juegos de Mesa
        8 - Instrumentos Musicales
        9 - Drones y Tecnología
        10 - Material Didáctico
        """)

    # Método para agregar un nuevo producto a la base de datos.
    def agregar_producto(self):
        # Solicitamos al usuario los datos del nuevo producto.
        nombreProducto = str(input("Ingrese el nombre del producto: "))
        descripcionProducto = str(input("Ingrese la descripcion del Producto o deje en blanco: "))

        try:
            # Solicitamos el stock, precio y categoría del producto.
            stock = int(input("Ingrese el stock del producto: "))
            precio = int(input("Ingrese el precio del producto: "))
            # Mostramos las categorías disponibles para que el usuario elija una.
            self.mostrar_categorias()
            idCategoria = int(input("Ingrese el ID de la categoría del producto: "))
        except ValueError:
            # Si el usuario no ingresa un número válido, mostramos un mensaje de error.
            print("El stock, precio y categoría deben ser números enteros.")
            return

        # Validamos que los datos ingresados sean correctos.
        if len(nombreProducto) > 0 and stock > 0 and precio > 0 and 1 <= idCategoria <= 10:
            try:
                # Verificamos si la categoría ingresada existe en la base de datos.
                resultado_categoria = db.ejecutar_consulta("SELECT * FROM categoria WHERE idCategoria = ?", (idCategoria,))
                if not resultado_categoria.fetchone():
                    print(f"Error: El ID de categoría {idCategoria} no existe. Ingrese una categoría válida.")
                    return

                # Si los datos son correctos, insertamos el nuevo producto en la base de datos.
                sql = "INSERT INTO producto(nombreProducto, descripcionProducto, stock, precio, idCategoria) VALUES (?, ?, ?, ?, ?)"
                parametros = (nombreProducto, descripcionProducto, stock, precio, idCategoria)
                db.ejecutar_consulta(sql, parametros)
                print(f"Producto '{nombreProducto}' ingresado correctamente.")
            except Exception as e:
                # Mostramos un mensaje de error en caso de que ocurra un problema al insertar el producto.
                print(f"Error al insertar el producto: {e}")
        else:
            # Mostramos un mensaje de error si los datos no son válidos.
            print("Datos incorrectos, intente de nuevo.")

    # Método para mostrar todos los productos registrados en la base de datos.
    def mostrar_productos(self):
        print("Mostrando productos...")
        # Ejecutamos una consulta para obtener todos los productos de la base de datos.
        result = db.ejecutar_consulta("SELECT * FROM producto")
        for data in result:
            # Mostramos la información de cada producto.
            print(f"""
                Id producto: {data[0]}
                Nombre del producto: {data[1]}
                Descripción del producto: {data[2]}
                Precio: {data[3]}
                Stock: {data[4]}
                Id categoría: {data[5]}
            """)

    # Método para modificar un producto existente.
    def modificar_producto(self):
        try:
            # Solicitamos el ID del producto que se desea modificar.
            idProducto = int(input("Ingrese el ID del producto que desea modificar: "))
            # Ejecutamos una consulta para obtener los datos del producto.
            resultado = db.ejecutar_consulta("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
            producto = resultado.fetchone()

            if producto is None:
                # Si el producto no existe, mostramos un mensaje de error.
                print(f"No existe un producto con el ID {idProducto}.")
                return

            # Mostramos la información actual del producto al usuario.
            print(f"""
            Producto actual:
            Id producto: {producto[0]}
            Nombre del producto: {producto[1]}
            Descripción del producto: {producto[2]}
            Stock: {producto[3]}
            Precio: {producto[4]}
            Id categoría: {producto[5]}
            """)

            # Solicitamos los nuevos datos del producto (con opción de dejar valores sin modificar).
            nombreProducto = input(f"Ingrese el nuevo nombre del producto (deje en blanco para mantener '{producto[1]}'): ") or producto[1]
            descripcionProducto = input(f"Ingrese la nueva descripción del producto (deje en blanco para mantener '{producto[2]}'): ") or producto[2]

            try:
                # Solicitamos el nuevo stock y precio (validando que sean valores correctos).
                stock = input(f"Ingrese el nuevo stock (deje en blanco para mantener '{producto[3]}'): ") or producto[3]
                stock = int(stock) if stock else producto[3]

                precio = input(f"Ingrese el nuevo precio (deje en blanco para mantener '{producto[4]}'): ") or producto[4]
                precio = float(precio) if precio else producto[4]

                idCategoria = input(f"Ingrese el nuevo ID de la categoría (deje en blanco para mantener '{producto[5]}'): ") or producto[5]
                idCategoria = int(idCategoria) if idCategoria else producto[5]

            except ValueError:
                # Si los datos no son válidos, mostramos un mensaje de error.
                print("El stock, precio e ID de la categoría deben ser números válidos.")
                return

            # Validamos los nuevos datos.
            if stock < 0 or precio < 0 or idCategoria < 1 or idCategoria > 10:
                # Si los datos no son válidos, mostramos un mensaje de error.
                print("El stock, precio o ID de la categoría no son válidos. Por favor, ingrese valores positivos y un ID de categoría válido.")
                return

            # Actualizamos el producto en la base de datos con los nuevos valores.
            sql = """UPDATE producto
                    SET nombreProducto = ?, descripcionProducto = ?, stock = ?, precio = ?, idCategoria = ?
                    WHERE idProducto = ?"""
            parametros = (nombreProducto, descripcionProducto, stock, precio, idCategoria, idProducto)
            db.ejecutar_consulta(sql, parametros)
            print(f"Producto '{nombreProducto}' actualizado correctamente.")

        except ValueError:
            # Si el ID del producto no es válido, mostramos un mensaje de error.
            print("El ID del producto debe ser un número válido.")
        except Exception as e:
            # Mostramos un mensaje de error en caso de que ocurra un problema durante la modificación.
            print(f"Error al modificar el producto: {e}")

    # Método para eliminar un producto de la base de datos.
    def eliminar_producto(self):
        try:
            # Solicitamos el ID del producto que se desea eliminar.
            idProducto = int(input("Ingrese el ID del producto que desea eliminar: "))
            # Ejecutamos una consulta para obtener los datos del producto.
            resultado = db.ejecutar_consulta("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
            producto = resultado.fetchone()

            if producto is None:
                # Si el producto no existe, mostramos un mensaje de error.
                print(f"No existe un producto con el ID {idProducto}.")
                return

            # Mostramos la información del producto a eliminar.
            print(f"""
            Producto a eliminar:
            Id producto: {producto[0]}
            Nombre del producto: {producto[1]}
            Descripción del producto: {producto[2]}
            Stock: {producto[3]}
            Precio: {producto[4]}
            Id categoría: {producto[5]}
            """)

            # Confirmamos si el usuario realmente desea eliminar el producto.
            confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()
            if confirmacion == 's':
                # Si el usuario confirma, eliminamos el producto de la base de datos.
                sql = "DELETE FROM producto WHERE idProducto = ?"
                db.ejecutar_consulta(sql, (idProducto,))
                print(f"Producto con ID {idProducto} eliminado correctamente.")
            else:
                # Si el usuario cancela la operación.
                print("Operación cancelada.")

        except ValueError:
            # Si el ID del producto no es válido, mostramos un mensaje de error.
            print("El ID del producto debe ser un número válido.")
        except Exception as e:
            # Mostramos un mensaje de error en caso de que ocurra un problema durante la eliminación.
            print(f"Error al eliminar el producto: {e}")
