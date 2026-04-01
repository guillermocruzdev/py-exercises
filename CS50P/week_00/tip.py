# https://cs50.harvard.edu/python/psets/0/tip/

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    valor = float(d.replace('$',''))
    return valor


def percent_to_float(p):
    valor = float(p.replace('%',''))
    porciento = valor / 100
    return porciento


main()
