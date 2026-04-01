# https://cs50.harvard.edu/python/psets/0/playback/

def puntos(texto):
    return texto.replace(' ','...')

def main():
    entrada = input('Ingrese un texto: ')
    resultado = puntos(entrada)
    print(resultado)

main()