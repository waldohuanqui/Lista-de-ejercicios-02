import os

def listar_carpetas(path):
    elementos = os.listdir(path)
    for elemento in elementos:
        elemento_path = os.path.join(path, elemento)
        if os.path.isdir(elemento_path):
            listar_carpetas(elemento_path)
        else:
            print(elemento_path)

listar_carpetas('/home/waldo/Documentos/Python certifiate example')