# Importamos el módulo CRUD que maneja la conexión a la base de datos
import CRUD as conn
# Importamos las clases de métodos de pago para procesar transacciones (TarjetaCredito, PayPal, TransferenciaBancaria)
from pagos import TarjetaCredito, PayPal, TransferenciaBancaria
# Establecemos una conexión con la base de datos a través del módulo CRUD
db = conn.Database()

# Clase que maneja el proceso de compra en la tienda
class ProcesoCompra:
    def __init__(self):
        # Inicializamos el carrito de compras como una lista vacía
        self.carrito = []

    # Método para mostrar el menú del proceso de compra con diferentes opciones
    def mostrar_menu_proceso_compra(self):
        while True:
            # Imprimimos el menú con las opciones disponibles
            print("\t===============================")
            print("Proceso de compra")
            print("\t===============================")
            print("[1] Buscar Producto")
            print("[2] Agregar Producto al Carrito")
            print("[3] Ver Carrito")
            print("[4] Completar Transacción")
            print("[5] Volver al menú principal")
            print("\t===============================")

            try:
                # Capturamos la opción seleccionada por el usuario
                option = int(input("Selecciona una opción: "))
                if option == 1:
                    # Opción para buscar un producto en la base de datos
                    self.buscarProducto()
                elif option == 2:
                    # Opción para agregar un producto al carrito ingresando su ID
                    idProducto = int(input("Ingrese el ID del producto que desea agregar: "))
                    self.agregarProductoAlCarrito(idProducto)
                elif option == 3:
                    # Opción para ver el contenido del carrito
                    self.verCompra()
                elif option == 4:
                    # Opción para completar la transacción
                    self.completarTransaccion()
                elif option == 5:
                    # Opción para volver al menú principal
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    # Método para buscar un producto en la base de datos
    def buscarProducto(self):
        # Solicitamos el nombre del producto al usuario
        producto = input("Ingrese el nombre del producto que desea buscar: ")
        # Ejecutamos una consulta para buscar el producto por su nombre
        query = "SELECT * FROM producto WHERE nombreProducto LIKE ?"
        result = db.ejecutar_consulta(query, ('%' + producto + '%',))
        productos_encontrados = result.fetchall()

        if productos_encontrados:
            # Mostramos los productos encontrados
            print("Productos encontrados:")
            for prod in productos_encontrados:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Descripción: {prod[2]}, Precio: {prod[4]}, Stock: {prod[3]}")
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para agregar un producto al carrito de compras utilizando su ID
    def agregarProductoAlCarrito(self, idProducto):
        # Buscamos el producto en la base de datos por su ID
        query = "SELECT * FROM producto WHERE idProducto = ?"
        result = db.ejecutar_consulta(query, (idProducto,))
        producto = result.fetchone()

        if producto:
            # Si se encuentra el producto, lo agregamos al carrito
            self.carrito.append(producto)
            print(f"Producto '{producto[1]}' agregado al carrito.")
        else:
            print(f"No existe un producto con el ID {idProducto}.")

    # Método para mostrar el contenido del carrito
    def verCompra(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.carrito:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[4]}, Stock: {producto[3]}")

    # Método para seleccionar el método de pago
    def seleccionar_metodo_pago(self, total):
        """Permite seleccionar el método de pago antes de completar la transacción"""
        print("\nTotal a pagar: ${}".format(total))
        print("Selecciona un método de pago:")
        print("[1] Tarjeta de crédito")
        print("[2] PayPal")
        print("[3] Transferencia bancaria")

        try:
            # Capturamos la opción seleccionada para el método de pago
            option = int(input("Selecciona una opción: "))
            if option == 1:
                # Capturamos los detalles de la tarjeta de crédito
                numero_tarjeta = input("Ingresa el número de la tarjeta: ")
                cvv = input("Ingresa el CVV: ")
                return TarjetaCredito(total, numero_tarjeta, cvv)
            elif option == 2:
                # Capturamos el correo electrónico para el pago por PayPal
                email = input("Ingresa tu correo de PayPal: ")
                return PayPal(total, email)
            elif option == 3:
                # Capturamos el número de cuenta para la transferencia bancaria
                numero_cuenta = input("Ingresa el número de cuenta bancaria: ")
                return TransferenciaBancaria(total, numero_cuenta)
            else:
                print("Opción no válida.")
                return None
        except ValueError:
            print("Error: Debes seleccionar una opción válida.")
            return None

    # Método para completar la transacción
    def completarTransaccion(self):
        if not self.carrito:
            print("No hay productos en el carrito para completar la compra.")
            return

        # Calcular el total de la compra sumando los precios de los productos en el carrito
        total = sum(producto[4] for producto in self.carrito)

        # Seleccionar el método de pago
        metodo_pago = self.seleccionar_metodo_pago(total)
        if metodo_pago:
            # Procesar el pago
            print("Procesando el pago...")
            pago_exitoso = metodo_pago.procesar_pago()
            if not pago_exitoso:
                print("El pago no pudo ser procesado.")
                return

        # Si el pago es exitoso, actualizamos el stock y completamos la transacción
        try:
            for producto in self.carrito:
                idProducto = producto[0]
                stock_actual = producto[3]

                if stock_actual > 0:
                    # Actualizamos el stock del producto
                    nuevo_stock = stock_actual - 1
                    query = "UPDATE producto SET stock = ? WHERE idProducto = ?"
                    db.ejecutar_consulta(query, (nuevo_stock, idProducto))
                    print(f"Producto '{producto[1]}' actualizado: stock reducido a {nuevo_stock}.")
                else:
                    print(f"El producto '{producto[1]}' no tiene stock disponible.")
                    continue

            # Limpiamos el carrito tras completar la transacción
            print("Transacción completada. Gracias por su compra.")
            self.carrito.clear()

        except Exception as e:
            print(f"Error al completar la transacción: {e}")
