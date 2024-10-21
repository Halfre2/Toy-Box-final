import CRUD as conn
db = conn.Database()  # Se importa el módulo CRUD para la conexión con la base de datos

class Usuarios:
    def __init__(self):
        pass  # Clase Usuarios para organizar la gestión de usuarios

    class Usuario:
        def __init__(self, run, nombres, apellidos, correo, telefono, direccion, clave):
            # Atributos privados para encapsular datos sensibles
            self._run = run
            self.nombres = nombres  # No encapsulado, acceso público
            self.apellidos = apellidos  # No encapsulado, acceso público
            self._correo = correo  # Encapsulado
            self.telefono = telefono  # No encapsulado, acceso público
            self._direccion = direccion  # Encapsulado
            self._clave = clave  # Encapsulado

        # Getters para acceder a los atributos encapsulados
        def get_run(self):
            return self._run

        def get_correo(self):
            return self._correo

        def get_direccion(self):
            return self._direccion

        def get_clave(self):
            return self._clave

        # Setters para modificar los atributos encapsulados
        def set_run(self, run):
            self._run = run

        def set_correo(self, correo):
            self._correo = correo

        def set_direccion(self, direccion):
            self._direccion = direccion

        def set_clave(self, clave):
            self._clave = clave

    # Método para agregar un usuario a la base de datos
    def agregar_usuario(self):
        # Solicita los datos del usuario
        run = str(input("Ingrese el RUN del usuario: "))
        nombres = str(input("Ingrese los nombres del usuario: "))
        apellidos = str(input("Ingrese los apellidos del usuario: "))
        correo = str(input("Ingrese el correo del usuario: "))
        telefono = str(input("Ingrese el teléfono del usuario: "))
        direccion = str(input("Ingrese la dirección del usuario: "))
        clave = str(input("Ingrese la clave del usuario: "))

        # Verifica que los datos clave no estén vacíos
        if len(run) > 0 and len(nombres) > 0 and len(apellidos) > 0 and len(correo) > 0 and len(clave) > 0:
            try:
                # Inserta los datos del usuario en la tabla 'usuario'
                sql = "INSERT INTO usuario(run, nombres, apellidos, correo, telefono, direccion, clave) VALUES (?, ?, ?, ?, ?, ?, ?)"
                parametros = (run, nombres, apellidos, correo, telefono, direccion, clave)
                db.ejecutar_consulta(sql, parametros)
                print(f"Usuario '{nombres} {apellidos}' agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar el usuario: {e}")  # Manejo de errores en la inserción
        else:
            print("Datos incorrectos, intente de nuevo.")  # Validación de datos obligatorios

    # Método para buscar un usuario por RUN
    def buscar_usuario(self):
        # Solicita el RUN del usuario que se desea buscar
        run = str(input("Ingrese el RUN del usuario que desea buscar: "))
        resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
        usuario = resultado.fetchone()

        # Si el usuario existe, se muestra
        if usuario:
            # Se crea un objeto de la clase Usuario con los datos obtenidos
            usuario_obj = self.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
            # Se muestran los datos del usuario utilizando los getters para los atributos encapsulados
            print(f"""
            Usuario encontrado:
            RUN: {usuario_obj.get_run()}
            Nombres: {usuario_obj.nombres}
            Apellidos: {usuario_obj.apellidos}
            Correo: {usuario_obj.get_correo()}
            Teléfono: {usuario_obj.telefono}
            Dirección: {usuario_obj.get_direccion()}
            Clave: {usuario_obj.get_clave()}
            """)
        else:
            print(f"No se encontró un usuario con el RUN {run}.")  # Mensaje si no existe el usuario

    # Método para modificar un usuario existente
    def modificar_usuario(self):
        try:
            # Solicita el RUN del usuario que se desea modificar
            run = str(input("Ingrese el RUN del usuario que desea modificar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
            usuario = resultado.fetchone()

            # Verifica si el usuario existe
            if usuario is None:
                print(f"No existe un usuario con el RUN {run}.")
                return

            # Crea un objeto de la clase Usuario con los datos existentes
            usuario_obj = self.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])

            # Muestra los datos actuales del usuario
            print(f"""
            Usuario actual:
            RUN: {usuario_obj.get_run()}
            Nombres: {usuario_obj.nombres}
            Apellidos: {usuario_obj.apellidos}
            Correo: {usuario_obj.get_correo()}
            Teléfono: {usuario_obj.telefono}
            Dirección: {usuario_obj.get_direccion()}
            Clave: {usuario_obj.get_clave()}
            """)

            # Solicita los nuevos valores, dejando los actuales si no se ingresa nada
            nuevos_nombres = input(f"Ingrese los nuevos nombres del usuario (deje en blanco para mantener '{usuario_obj.nombres}'): ") or usuario_obj.nombres
            nuevos_apellidos = input(f"Ingrese los nuevos apellidos del usuario (deje en blanco para mantener '{usuario_obj.apellidos}'): ") or usuario_obj.apellidos
            nuevo_correo = input(f"Ingrese el nuevo correo del usuario (deje en blanco para mantener '{usuario_obj.get_correo()}'): ") or usuario_obj.get_correo()
            nuevo_telefono = input(f"Ingrese el nuevo teléfono del usuario (deje en blanco para mantener '{usuario_obj.telefono}'): ") or usuario_obj.telefono
            nueva_direccion = input(f"Ingrese la nueva dirección del usuario (deje en blanco para mantener '{usuario_obj.get_direccion()}'): ") or usuario_obj.get_direccion()
            nueva_clave = input(f"Ingrese la nueva clave del usuario (deje en blanco para mantener la clave actual): ") or usuario_obj.get_clave()

            # Actualiza los atributos del objeto usuario
            usuario_obj.nombres = nuevos_nombres
            usuario_obj.apellidos = nuevos_apellidos
            usuario_obj.set_correo(nuevo_correo)
            usuario_obj.telefono = nuevo_telefono
            usuario_obj.set_direccion(nueva_direccion)
            usuario_obj.set_clave(nueva_clave)

            # Actualiza los datos en la base de datos
            sql = """UPDATE usuario
                    SET nombres = ?, apellidos = ?, correo = ?, telefono = ?, direccion = ?, clave = ?
                    WHERE run = ?"""
            parametros = (usuario_obj.nombres, usuario_obj.apellidos, usuario_obj.get_correo(), usuario_obj.telefono, usuario_obj.get_direccion(), usuario_obj.get_clave(), usuario_obj.get_run())
            db.ejecutar_consulta(sql, parametros)
            print(f"Usuario '{usuario_obj.nombres} {usuario_obj.apellidos}' actualizado correctamente.")
        except ValueError:
            print("El RUN del usuario debe ser válido.")  # Manejo de errores de valor
        except Exception as e:
            print(f"Error al modificar el usuario: {e}")

    # Método para eliminar un usuario por RUN
    def eliminar_usuario(self):
        try:
            # Solicita el RUN del usuario a eliminar
            run = str(input("Ingrese el RUN del usuario que desea eliminar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
            usuario = resultado.fetchone()

            # Verifica si el usuario existe
            if usuario is None:
                print(f"No existe un usuario con el RUN {run}.")
                return

            # Crea un objeto de la clase Usuario con los datos existentes
            usuario_obj = self.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
            
            # Muestra los datos del usuario a eliminar
            print(f"""
            Usuario a eliminar:
            RUN: {usuario_obj.get_run()}
            Nombres: {usuario_obj.nombres}
            Apellidos: {usuario_obj.apellidos}
            Correo: {usuario_obj.get_correo()}
            Teléfono: {usuario_obj.telefono}
            Dirección: {usuario_obj.get_direccion()}
            Clave: {usuario_obj.get_clave()}
            """)

            confirmacion = input("¿Está seguro que desea eliminar este usuario? (s/n): ").lower()
            if confirmacion == 's':
                # Elimina el usuario de la base de datos
                sql = "DELETE FROM usuario WHERE run = ?"
                db.ejecutar_consulta(sql, (run,))
                print(f"Usuario con RUN {run} eliminado correctamente.")
            else:
                print("Operación cancelada.")
        except ValueError:
            print("El RUN del usuario debe ser válido.")
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")

    # Método para mostrar todos los usuarios registrados
    def ver_usuarios(self):
        # Consulta todos los usuarios en la base de datos
        print("Mostrando todos los usuarios...")
        resultado = db.ejecutar_consulta("SELECT * FROM usuario")
        usuarios = resultado.fetchall()

        if usuarios:
            # Itera sobre todos los usuarios y los muestra
            for usuario in usuarios:
                usuario_obj = self.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
                print(f"""
                RUN: {usuario_obj.get_run()}
                Nombres: {usuario_obj.nombres}
                Apellidos: {usuario_obj.apellidos}
                Correo: {usuario_obj.get_correo()}
                Teléfono: {usuario_obj.telefono}
                Dirección: {usuario_obj.get_direccion()}
                Clave: {usuario_obj.get_clave()}
                """)
        else:
            print("No hay usuarios registrados.")
