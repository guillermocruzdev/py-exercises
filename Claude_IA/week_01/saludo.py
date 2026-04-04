# Ejercicio 1
# Escribe una función que reciba un nombre y salude
# Ejemplo: saludar("Carlos") debe imprimir "Hola, Carlos"

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar(input("¿Cuál es tu nombre? ").title())