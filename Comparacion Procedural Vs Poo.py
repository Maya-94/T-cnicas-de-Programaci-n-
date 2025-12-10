#!/usr/bin/env python3
"""
Comparación: Programación Tradicional (Procedural) vs Programación Orientada a Objetos (POO)
Archivo: Comparacion_Procedural_vs_POO.py

Contenido:
- Implementación procedural (funciones) para leer temperaturas diarias y calcular promedio semanal.
- Implementación en POO con clases, encapsulamiento, herencia y polimorfismo simples.

Instrucciones de uso:
- Ejecuta: python Comparacion_Procedural_vs_POO.py
- Sigue el menú para probar la versión procedural o la versión OOP.

Este archivo incluye comentarios paso a paso explicando la lógica.
"""

# =====================
# 1) Programación Tradicional
# =====================

def leer_temperaturas_dias(desde_dia=1, hasta_dia=7, pedir_por_input=True, muestra=None):
    """
    Lee temperaturas para una semana (7 días) y las devuelve en una lista.

    Parámetros:
    - desde_dia, hasta_dia: rangos (por si se desea variar el número de días).
    - pedir_por_input: si True pide valores al usuario vía input(); si False usa 'muestra' si está provista.
    - muestra: lista de floats usada cuando pedir_por_input==False (para pruebas automatizadas).

    Retorna: lista de floats con las temperaturas diarias.
    """
    n = hasta_dia - desde_dia + 1
    temperaturas = []

    if not pedir_por_input and muestra is not None:
        # Validar longitud
        if len(muestra) < n:
            raise ValueError(f"Se esperaban {n} temperaturas en 'muestra', recibidas {len(muestra)}")
        return [float(x) for x in muestra[:n]]

    # Interacción con el usuario: pedir n temperaturas
    for i in range(n):
        while True:
            try:
                entrada = input(f"Temperatura día {desde_dia + i}: ")
                temp = float(entrada)
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Introduce un número (ej: 23.5)")
    return temperaturas


def calcular_promedio(lista):
    """Calcula el promedio de una lista de números. Maneja lista vacía lanzando ValueError."""
    if not lista:
        raise ValueError("La lista está vacía; no se puede calcular el promedio.")
    return sum(lista) / len(lista)


def procedimiento_tradicional_demo(muestra=None):
    """
    Demostración de la solución procedimental:
    - lee temperaturas (por input o usando 'muestra')
    - calcula el promedio semanal
    - muestra resultados
    """
    print("\n--- Versión Procedural (Funciones) ---")
    try:
        temps = leer_temperaturas_dias(pedir_por_input=(muestra is None), muestra=muestra)
        promedio = calcular_promedio(temps)
        print(f"Temperaturas: {temps}")
        print(f"Promedio semanal: {promedio:.2f}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# =====================
# 2) Programación Orientada a Objetos (POO)
# =====================

class WeatherDay:
    """
    Clase que representa la información diaria del clima.

    Atributos:
    - _temperature: (float) temperatura del día (privado con guion bajo para mostrar encapsulamiento simple).
    - day_index: entero para identificar el día dentro de la semana (opcional).

    Métodos principales:
    - set_temperature(value): valida y guarda la temperatura.
    - get_temperature(): retorna la temperatura.
    """

    def __init__(self, temperature: float = None, day_index: int = None):
        self._temperature = None
        self.day_index = day_index
        if temperature is not None:
            self.set_temperature(temperature)

    def set_temperature(self, value):
        # Validación simple: temperatura debe ser numérica
        try:
            val = float(value)
        except Exception:
            raise ValueError("Temperature debe ser numérica")
        self._temperature = val

    def get_temperature(self):
        return self._temperature

    def __repr__(self):
        return f"WeatherDay(day={self.day_index}, temp={self._temperature})"


class WeeklyWeather:
    """
    Clase que acumula WeatherDay para una semana y calcula promedios.

    Encapsula la lista de días en un atributo privado.
    """
    def __init__(self, days_expected=7):
        self._days = []  # atributo privado
        self.days_expected = days_expected

    def add_day(self, weather_day: WeatherDay):
        """Agrega un WeatherDay validando tipo y límite de días."""
        if not isinstance(weather_day, WeatherDay):
            raise TypeError("Se esperaba un objeto WeatherDay")
        if len(self._days) >= self.days_expected:
            raise ValueError("Ya se alcanzó el número máximo de días")
        self._days.append(weather_day)

    def from_list(self, temps_list):
        """Conveniencia para llenar la semana desde una lista de números."""
        if len(temps_list) != self.days_expected:
            raise ValueError(f"Se esperan {self.days_expected} temperaturas, recibidas {len(temps_list)}")
        self._days = [WeatherDay(temp, i + 1) for i, temp in enumerate(temps_list)]

    def average(self):
        """Calcula y retorna el promedio de las temperaturas almacenadas."""
        if not self._days:
            raise ValueError("No hay datos de días para calcular promedio")
        total = sum(d.get_temperature() for d in self._days)
        return total / len(self._days)

    def __len__(self):
        return len(self._days)

    def __repr__(self):
        return f"WeeklyWeather({self._days})"


# Ejemplo sencillo de herencia y polimorfismo:
class AnnotatedWeeklyWeather(WeeklyWeather):
    """
    Subclase que añade una anotación (por ejemplo: semana "Fría", "Cálida")
    y demuestra polimorfismo sobre el método average mostrando un string formateado.
    """
    def __init__(self, label: str = None, days_expected=7):
        super().__init__(days_expected=days_expected)
        self.label = label

    def average(self):
        """
        Sobrescribe average para devolver un diccionario con más contexto.
        Esto demuestra polimorfismo: el mismo método 'average' tiene distinto comportamiento
        dependiendo de la clase.
        """
        base_avg = super().average()
        return {"label": self.label, "average": base_avg, "n_days": len(self._days)}


def procedimiento_poo_demo(muestra=None):
    """
    Demostración de la solución en POO.
    Si 'muestra' se proporciona (lista), se usa para poblar la semana; si no, se pide por input.
    """
    print("\n--- Versión POO (Clases) ---")
    try:
        week = WeeklyWeather(days_expected=7)
        if muestra is not None:
            week.from_list(muestra)
        else:
            temps = leer_temperaturas_dias(pedir_por_input=True)
            week.from_list(temps)

        avg = week.average()
        print(f"Objetos días: {week}")
        print(f"Promedio semanal (POO): {avg:.2f}")

        # Mostrar uso de la subclase con anotación
        annotated = AnnotatedWeeklyWeather(label="Semana de prueba", days_expected=7)
        if muestra is not None:
            annotated.from_list(muestra)
        else:
            annotated.from_list([d.get_temperature() for d in week._WeeklyWeather__dict__.get('_days', week._days)])
        annotated_result = annotated.average()
        print(f"Promedio con anotación (polimorfismo): {annotated_result}")

    except Exception as e:
        print(f"Ocurrió un error en POO: {e}")


# =====================
# 3) Menú de ejecución y ejemplo de pruebas
# =====================

def demo_con_muestra():
    """Ejecuta ambas implementaciones con datos de ejemplo para facilitar pruebas automáticas."""
    ejemplo = [20.5, 22.0, 19.5, 21.0, 23.2, 18.9, 20.0]
    print("\n> Ejecutando demo procedimental con muestra... ")
    procedimiento_tradicional_demo(muestra=ejemplo)
    print("\n> Ejecutando demo POO con la misma muestra... ")
    procedimiento_poo_demo(muestra=ejemplo)


def main():
    print("Comparación: Programación Tradicional vs POO")
    print("Elige una opción:")
    print("1) Demo procedural (pide por teclado)")
    print("2) Demo POO (pide por teclado)")
    print("3) Demo rápida con datos de ejemplo (no pide teclado)")
    print("4) Salir")

    opcion = input("Opción: ")
    if opcion == "1":
        procedimiento_tradicional_demo()
    elif opcion == "2":
        procedimiento_poo_demo()
    elif opcion == "3":
        demo_con_muestra()
    else:
        print("Saliendo. ¡Hasta luego!")


if __name__ == '__main__':
    main()
