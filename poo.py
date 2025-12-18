"""
POO – Cálculo del promedio semanal del clima
Autor: (Tu nombre)
Descripción:
    Este programa utiliza Programación Orientada a Objetos para registrar
    temperaturas diarias y calcular el promedio semanal.

Conceptos aplicados:
    - Encapsulamiento
    - Clases y objetos
    - Métodos
    - Herencia y polimorfismo (subclase que modifica el comportamiento)
"""

# -------------------------
# Clase que representa un día de clima
# -------------------------

class WeatherDay:
    def __init__(self, temperature=None, day_number=None):
        self._temperature = None        # Encapsulamiento (atributo privado)
        self.day_number = day_number
        if temperature is not None:
            self.set_temperature(temperature)

    def set_temperature(self, value):
        """Valida y asigna la temperatura del día."""
        try:
            self._temperature = float(value)
        except ValueError:
            raise ValueError("La temperatura debe ser un número.")

    def get_temperature(self):
        """Devuelve la temperatura almacenada."""
        return self._temperature

    def __repr__(self):
        return f"WeatherDay(día={self.day_number}, temp={self._temperature})"


# -------------------------
# Clase que representa la semana completa
# -------------------------

class WeeklyWeather:
    def __init__(self, days_expected=7):
        self._days = []                 # Lista privada (encapsulada)
        self.days_expected = days_expected

    def add_day(self, weather_day):
        """Agrega un objeto WeatherDay validando el tipo."""
        if not isinstance(weather_day, WeatherDay):
            raise TypeError("Se debe agregar un objeto WeatherDay.")
        if len(self._days) >= self.days_expected:
            raise ValueError("Ya se registraron todos los días.")
        self._days.append(weather_day)

    def from_list(self, temps):
        """Llena la semana desde una lista de temperaturas."""
        if len(temps) != self.days_expected:
            raise ValueError("La lista no tiene la cantidad correcta de días.")
        self._days = []
        for i, t in enumerate(temps):
            self._days.append(WeatherDay(t, i + 1))

    def average(self):
        """Calcula el promedio semanal."""
        if not self._days:
            raise ValueError("No hay datos cargados.")
        total = sum(day.get_temperature() for day in self._days)
        return total / len(self._days)

    def __repr__(self):
        return f"WeeklyWeather({self._days})"


# -------------------------
# Herencia y polimorfismo
# -------------------------

class AnnotatedWeeklyWeather(WeeklyWeather):
    """Subclase que añade una etiqueta y modifica el método average (polimorfismo)."""

    def __init__(self, label, days_expected=7):
        super().__init__(days_expected)
        self.label = label

    def average(self):
        """Sobrescribe el método average añadiendo información extra."""
        base_avg = super().average()
        return f"Promedio = {base_avg:.2f} °C | Etiqueta: {self.label}"


# -------------------------
# Programa de demostración
# -------------------------

def main():
    print("\n=== Promedio semanal del clima (POO) ===")
    temps = []

    # Pedimos 7 temperaturas al usuario
    for i in range(7):
        while True:
            try:
                t = float(input(f"Ingrese temperatura del día {i+1}: "))
                temps.append(t)
                break
            except ValueError:
                print("Error: ingrese un número válido.")

    # Creamos el objeto semanal
    week = WeeklyWeather()
    week.from_list(temps)

    # Calculamos promedio
    prom = week.average()

    print("\nTemperaturas registradas:", temps)
    print(f"Promedio semanal: {prom:.2f} °C")

    # Demostración de la subclase
    print("\nDemostración de polimorfismo:")
    ann = AnnotatedWeeklyWeather("Semana de ejemplo")
    ann.from_list(temps)
    print(ann.average())


if __name__ == "__main__":
    main()
