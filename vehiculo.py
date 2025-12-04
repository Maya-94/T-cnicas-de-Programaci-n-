from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Auto(Vehiculo):
    def encender(self):
        return f"El auto {self.marca} {self.modelo} ha sido encendido."

    def apagar(self):
        return f"El auto {self.marca} {self.modelo} ha sido apagado."


# Ejemplo
if __name__ == "__main__":
    auto = Auto("Toyota", "Corolla")
    print(auto.encender())
    print(auto.apagar())
