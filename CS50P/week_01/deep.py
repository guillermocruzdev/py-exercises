# https://cs50.harvard.edu/python/psets/1/deep/

def deep(string):
    if string == '42' or string == 'forty-two' or string == 'forty two':
        print('Yes')
    else:
        print('No')

def main():
    deep(input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip())

main()