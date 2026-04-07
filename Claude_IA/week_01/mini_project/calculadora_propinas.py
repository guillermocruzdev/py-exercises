# CALCULADORA DE PROPINAS
# El programa debe:
# 1. Pedir el monto total de la cuenta
# 2. Pedir el porcentaje de propina que quieren dar (10, 15 o 20)
# 3. Pedir cuántas personas son
# 4. Calcular: propina total, total con propina, cuánto paga cada persona
# 5. Mostrar todo ordenado

# Ejemplo de salida esperada:
# Cuenta: $500
# Propina (15%): $75
# Total: $575
# Por persona (4 personas): $143.75


def limpiar_numero(texto):
    limpio = texto.replace('$', '').replace('%', '').strip()
    return float(limpio)

monto = limpiar_numero(input('Ingrese total de la cuenta: '))
porcentaje_propina = limpiar_numero(input('¿Cuanto desea agregar de propina? '))
personas = int(input('¿Cuantas personas son? '))

propina_total = monto * (porcentaje_propina / 100)
total = monto + propina_total
total_persona = total / personas

print(f'\nCuenta: ${monto:.2f}')
print(f'Propina ({porcentaje_propina:.0f}%): ${propina_total:.2f}')
print(f'Total: ${total:.2f}')
print(f'Por persona ({personas} personas): ${total_persona:.2f}')


