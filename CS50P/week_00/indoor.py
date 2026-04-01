# https://cs50.harvard.edu/python/psets/0/indoor/

def minusculas(texto):
    return texto.lower()

def main():
    entrada = input('Ingrese un texto: ')
    resultado = minusculas(entrada)
    print(resultado)

main()
