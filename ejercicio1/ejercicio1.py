def dibujar_cuadrado():
    lado = int(input("Ingrese la longitud del lado del cuadrado: "))
    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def imprimir_multiplos():
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in lista_numeros:
        if num % 2 == 0:
            print(num)

def imprimir_mayores_edad():
    lista_personas = [["Juan", 25], ["María", 17], ["Pedro", 33], ["Ana", 15], ["Luis", 20]]
    for persona in lista_personas:
        if persona[1] >= 18:
            print(persona[0])

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Dibujar cuadrado")
    print("2. Imprimir múltiplos de 2")
    print("3. Imprimir mayores de edad")
    opcion = input("Opción seleccionada: ")
    return opcion

opcion = mostrar_menu()

while opcion != "4":
    if opcion == "1":
        dibujar_cuadrado()
    elif opcion == "2":
        imprimir_multiplos()
    elif opcion == "3":
        imprimir_mayores_edad()
    else:
        print("Opción inválida")

    opcion = mostrar_menu()

print("Fin del programa")