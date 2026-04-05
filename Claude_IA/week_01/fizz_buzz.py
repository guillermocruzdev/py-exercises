# Ejercicio 2: Ciclos
# Imprime todos los números del 1 al 20
# pero si el número es divisible entre 3, imprime "fizz"
# y si es divisible entre 5, imprime "buzz"
# (esto es el clásico FizzBuzz — todo reclutador técnico lo conoce)

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print (i)

entrada = int(input('Ingrese un numero: '))
fizz_buzz(entrada)
    