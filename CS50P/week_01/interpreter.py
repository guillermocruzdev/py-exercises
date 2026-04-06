# https://cs50.harvard.edu/python/psets/1/interpreter/

def interpreter(expression):
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z
    else:
        return "Operador no válido"

def main():
    resultado = interpreter(input('Expression: '))
    print(resultado)

main()
