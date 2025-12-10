def leer_temperaturas(n=7):
    temps = []
    for i in range(n):
        while True:
            try:
                t = float(input(f"Temperatura día {i+1}: "))
                temps.append(t)
                break
            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")
    return temps

def calcular_promedio(lista):
    if not lista:
        raise ValueError("Lista vacía.")
    return sum(lista)/len(lista)

def main():
    temps = leer_temperaturas()
    prom = calcular_promedio(temps)
    print("Temperaturas:", temps)
    print(f"Promedio semanal: {prom:.2f}")

if __name__ == '__main__':
    main()
