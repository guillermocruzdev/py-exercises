# Ejercicio 3
# ¿Cuál es la diferencia entre esto?

def version_a(x):
    print(x * 2)

def version_b(x):
    return x * 2

# La función version_a imprime el resultado, mientras que version_b devuelve el resultado. Esto significa que version_a no puede ser reutilizada en otras expresiones, mientras que version_b sí puede serlo.
# Por ejemplo, si queremos usar el resultado de version_b para hacer otra operación, podemos hacerlo fácilmente:

resultado = version_b(5)  # resultado ahora es 10
print(resultado + 3)  # Esto imprimirá 13

# En cambio, si intentamos hacer lo mismo con version_a, no funcionará:

resultado = version_a(5)  # Esto imprimirá 10 pero resultado será None
print(resultado + 3)  # Esto dará un error porque resultado es None

