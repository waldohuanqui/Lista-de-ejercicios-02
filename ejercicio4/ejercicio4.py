import sys

def imprimir_argumentos(*args):
    for arg in args:
        print(arg)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    imprimir_argumentos(*args)

