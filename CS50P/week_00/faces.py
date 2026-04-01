# https://cs50.harvard.edu/python/psets/0/faces/

def convert(texto):
    resultado = texto.replace(':)', '🙂').replace(':(', '🙁')
    return resultado

def main():
    entrada = input('Ingrese un texto: ')
    resultado = convert(entrada)
    print(resultado)

main()
