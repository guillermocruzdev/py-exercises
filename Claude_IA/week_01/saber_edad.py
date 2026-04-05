# Ejercicio 1: Condicionales
# Escribe una función que reciba una edad y devuelva:
# "menor de edad" si tiene menos de 18
# "adulto" si tiene entre 18 y 64
# "adulto mayor" si tiene 65 o más

def saber_edad(edad):
    if edad < 18:
        print ('menor de edad')
    elif edad < 65: 
        print ('adulto')
    else:
        print ('adulto mayor')

entrada = int(input('Ingresa tu edad: '))
saber_edad(entrada)