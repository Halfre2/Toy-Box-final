# Clase base MetodoPago que define una estructura para diferentes tipos de pago.
class MetodoPago:
    def __init__(self, monto):
        # Inicializa la clase con un monto a pagar.
        self.monto = monto

    def procesar_pago(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases")


# Clase TarjetaCredito que hereda de MetodoPago.
class TarjetaCredito(MetodoPago):
    def __init__(self, monto, numero_tarjeta, cvv):
        # Llama al constructor de la clase padre MetodoPago para inicializar el monto.
        super().__init__(monto)
        # Inicializa los atributos específicos de la tarjeta de crédito.
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv

    def procesar_pago(self):
        """
        Sobrescribe el método procesar_pago para implementar la lógica de pago
        utilizando tarjeta de crédito.
        """
        print(f"Procesando pago de ${self.monto} con tarjeta de crédito {self.numero_tarjeta}...")
        return True  # Devuelve True si el pago se procesó correctamente.


# Clase PayPal que hereda de MetodoPago.
class PayPal(MetodoPago):
    def __init__(self, monto, email):
        # Llama al constructor de la clase padre MetodoPago para inicializar el monto.
        super().__init__(monto)
        # Inicializa el atributo específico del email vinculado a la cuenta PayPal.
        self.email = email

    def procesar_pago(self):
        """
        Sobrescribe el método procesar_pago para implementar la lógica de pago
        utilizando PayPal.
        """
        print(f"Procesando pago de ${self.monto} a través de PayPal para el correo {self.email}...")
        return True  # Devuelve True si el pago se procesó correctamente.


# Clase TransferenciaBancaria que hereda de MetodoPago.
class TransferenciaBancaria(MetodoPago):
    def __init__(self, monto, numero_cuenta):
        # Llama al constructor de la clase padre MetodoPago para inicializar el monto.
        super().__init__(monto)
        # Inicializa el atributo específico de la cuenta bancaria.
        self.numero_cuenta = numero_cuenta

    def procesar_pago(self):
        """
        Sobrescribe el método procesar_pago para implementar la lógica de pago
        utilizando una transferencia bancaria.
        """
        print(f"Procesando pago de ${self.monto} mediante transferencia bancaria a la cuenta {self.numero_cuenta}...")
        return True  # Devuelve True si el pago se procesó correctamente.
