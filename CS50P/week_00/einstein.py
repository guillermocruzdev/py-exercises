# https://cs50.harvard.edu/python/psets/0/einstein/

c = 300000000

def masa(valor):
    return valor * (c ** 2)

def main():
    m = int(input('m: '))
    energia = masa(m)
    print(energia)

main()
