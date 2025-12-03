class Figura:
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


# Ejemplo
if __name__ == "__main__":
    figuras = [Cuadrado(5), Circulo(3)]

    for f in figuras:
        print("Área:", f.area())
