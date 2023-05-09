def obtener_mayor():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
mayor = obtener_mayor()
print("El número mayor es:", mayor)