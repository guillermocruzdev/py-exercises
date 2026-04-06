# https://cs50.harvard.edu/python/psets/1/bank/

def saludo(s):
    s = s.strip().lower()
    if s.startswith('hello'):
        print('$0')
    elif s.startswith('h'):
        print('$20')
    else:
        print('$100')

def main():
    saludo(input('Greeting: '))

main()
