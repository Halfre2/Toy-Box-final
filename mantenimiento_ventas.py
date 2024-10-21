# Importamos el módulo CRUD para la conexión y ejecución de consultas con la base de datos.
import CRUD as conn
# Instanciamos la conexión a la base de datos.
db = conn.Database()

# Definimos la clase Ventas que manejará todas las operaciones relacionadas con las ventas.
class Ventas:
    def __init__(self):
        pass  # El constructor no necesita hacer nada especial por ahora.

    # Método para cambiar el estado de envío de una venta.
    def cambiar_estado_envio(self):
        try:
            # Solicitamos el ID de la venta al usuario.
            idVenta = int(input("Ingrese el ID de la venta que desea actualizar el estado de envío: "))
            # Consultamos la base de datos para obtener la venta con ese ID.
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()  # Obtenemos una sola venta.

            if venta is None:
                print(f"No existe una venta con el ID {idVenta}.")
                return

            # Mostramos la venta actual al usuario y su estado de envío.
            print(f"""
            Venta actual:
            ID Venta: {venta[0]}
            Estado de envío: {venta[3]}
            """)

            # Ofrecemos las opciones de estados de envío disponibles.
            print("Opciones de estado de envío:")
            print("[1] A la espera de envío")
            print("[2] En proceso de envío")
            print("[3] Entregado")

            # Capturamos la opción seleccionada por el usuario.
            opcion_estado = int(input("Selecciona una opción de estado: "))
            estado_envio = ""

            # Asignamos el nuevo estado de envío según la opción seleccionada.
            if opcion_estado == 1:
                estado_envio = "A la espera de envío"
            elif opcion_estado == 2:
                estado_envio = "En proceso de envío"
            elif opcion_estado == 3:
                estado_envio = "Entregado"
            else:
                print("Opción de estado no válida.")
                return

            # Actualizamos el estado de envío en la base de datos.
            sql = "UPDATE venta SET estadoEnvio = ? WHERE idVenta = ?"
            parametros = (estado_envio, idVenta)
            db.ejecutar_consulta(sql, parametros)
            print(f"Estado de envío de la venta con ID {idVenta} actualizado a '{estado_envio}' correctamente.")

        except ValueError:
            # Controlamos si el usuario ingresa un valor no válido.
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            # Capturamos cualquier otro error inesperado.
            print(f"Error al cambiar el estado de envío: {e}")

    # Método para buscar una venta por su ID.
    def buscar_venta(self):
        try:
            # Solicitamos el ID de la venta que se desea buscar.
            idVenta = int(input("Ingrese el ID de la venta que desea buscar: "))
            # Ejecutamos la consulta para obtener la venta correspondiente.
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()  # Obtenemos la venta.

            if venta:
                # Si se encuentra la venta, la mostramos al usuario.
                print(f"""
                Venta encontrada:
                ID Venta: {venta[0]}
                Fecha de Venta: {venta[1]}
                Estado de Envío: {venta[3]}
                """)
            else:
                # Si no se encuentra la venta, lo indicamos.
                print(f"No se encontró una venta con el ID {idVenta}.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al buscar la venta: {e}")

    # Método para ver los detalles de una venta en particular.
    def ver_detalle_venta(self):
        try:
            # Solicitamos el ID de la venta cuyo detalle queremos ver.
            idVenta = int(input("Ingrese el ID de la venta cuyo detalle desea ver: "))
            # Ejecutamos la consulta para obtener los detalles de la venta.
            resultado = db.ejecutar_consulta("SELECT * FROM detalle_venta WHERE idVenta = ?", (idVenta,))
            detalles = resultado.fetchall()  # Obtenemos todos los detalles.

            if detalles:
                # Si hay detalles, los mostramos al usuario.
                for detalle in detalles:
                    print(f"""
                    Detalle de Venta:
                    ID Venta: {detalle[0]}
                    ID Producto: {detalle[1]}
                    Cantidad: {detalle[2]}
                    Precio Unitario: {detalle[3]}
                    """)
            else:
                # Si no hay detalles para esa venta, lo indicamos.
                print(f"No hay detalles registrados para la venta con ID {idVenta}.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al ver el detalle de la venta: {e}")

    # Método para eliminar una venta.
    def eliminar_venta(self):
        try:
            # Solicitamos el ID de la venta que se desea eliminar.
            idVenta = int(input("Ingrese el ID de la venta que desea eliminar: "))
            # Verificamos si la venta existe en la base de datos.
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()

            if venta is None:
                print(f"No existe una venta con el ID {idVenta}.")
                return

            # Mostramos la venta que será eliminada.
            print(f"""
            Venta a eliminar:
            ID Venta: {venta[0]}
            Fecha de Venta: {venta[1]}
            Estado de Envío: {venta[3]}
            """)

            # Pedimos confirmación para eliminar la venta.
            confirmacion = input("¿Está seguro que desea eliminar esta venta? (s/n): ").lower()
            if confirmacion == 's':
                # Si confirma, eliminamos la venta de la base de datos.
                sql = "DELETE FROM venta WHERE idVenta = ?"
                db.ejecutar_consulta(sql, (idVenta,))
                print(f"Venta con ID {idVenta} eliminada correctamente.")
            else:
                # Si cancela la operación.
                print("Operación cancelada.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")

    # Método para mostrar todas las ventas registradas.
    def ver_ventas(self):
        print("Mostrando todas las ventas...")
        # Ejecutamos la consulta para obtener todas las ventas.
        resultado = db.ejecutar_consulta("SELECT * FROM venta")
        ventas = resultado.fetchall()  # Obtenemos todas las ventas.

        if ventas:
            # Si hay ventas registradas, las mostramos.
            for venta in ventas:
                print(f"""
                ID Venta: {venta[0]}
                Fecha de Venta: {venta[1]}
                Estado de Envío: {venta[3]}
                """)
        else:
            # Si no hay ventas, lo indicamos.
            print("No hay ventas registradas.")

    # Menú de opciones para las operaciones de ventas.
    def mostrar_menu_ventas(self):
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
                # Capturamos la opción seleccionada por el usuario.
                option = int(input("Selecciona una opción: "))

                # Ejecutamos la función correspondiente según la opción seleccionada.
                if option == 1:
                    self.cambiar_estado_envio()
                elif option == 2:
                    self.buscar_venta()
                elif option == 3:
                    self.ver_detalle_venta()
                elif option == 4:
                    self.eliminar_venta()
                elif option == 5:
                    self.ver_ventas()
                elif option == 6:
                    break  # Volvemos al menú anterior.
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")
