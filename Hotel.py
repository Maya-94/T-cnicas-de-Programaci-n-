# archivo: hotel.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            print(f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}")
        else:
            print("La habitación no está disponible")


# Programa principal
habitacion1 = Habitacion(101, "Simple", 30)
cliente1 = Cliente("María Pianda", "0102030405")

reserva1 = Reserva(cliente1, habitacion1)
reserva1.confirmar_reserva()
