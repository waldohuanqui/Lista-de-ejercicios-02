biblioteca = {
    "Categoria 1": [
        {"titulo": "Libro 1", "autor": "Autor 1", "prestado": False},
        {"titulo": "Libro 2", "autor": "Autor 2", "prestado": True},
        {"titulo": "Libro 3", "autor": "Autor 3", "prestado": False}
    ],
    "Categoria 2": [
        {"titulo": "Libro 4", "autor": "Autor 4", "prestado": False},
        {"titulo": "Libro 5", "autor": "Autor 5", "prestado": False},
        {"titulo": "Libro 6", "autor": "Autor 6", "prestado": True}
    ]
}

def obtener_categorias():
    categorias = []
    for categoria in biblioteca:
        categorias.append(categoria)
    return categorias

def obtener_libros():
    libros = []
    for categoria in biblioteca:
        for libro in biblioteca[categoria]:
            libros.append((libro["titulo"], libro["autor"]))
    return libros

def prestar_libro(titulo):
    for categoria in biblioteca:
        for libro in biblioteca[categoria]:
            if libro["titulo"] == titulo:
                libro["prestado"] = True
                return True
    return False

def obtener_usuarios():
    return ["Usuario 1", "Usuario 2", "Usuario 3"]

# Ejemplo de uso
categorias = obtener_categorias()
print("Categorías:")
print(categorias)

libros = obtener_libros()
print("Libros:")
for libro in libros:
    print(libro[0], "de", libro[1])

libro_prestado = "Libro 3"
if prestar_libro(libro_prestado):
    print("Se ha prestado el libro", libro_prestado)
else:
    print("No se encontró el libro", libro_prestado)

usuarios = obtener_usuarios()
print("Usuarios:")
for usuario in usuarios:
    print(usuario)