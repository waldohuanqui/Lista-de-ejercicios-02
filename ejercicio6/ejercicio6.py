def main():
    detalles_evento = obtener_detalles_evento()
    
    if validar_detalles_evento(detalles_evento):
        guardar_evento(detalles_evento)
        print("Evento guardado exitosamente.")
    else:
        print("Error: detalles de evento no válidos.")
        
def obtener_detalles_evento():
    detalles_evento = {}
    detalles_evento['nombre'] = input("Ingrese el nombre del evento: ")
    detalles_evento['fecha'] = input("Ingrese la fecha del evento (dd/mm/aaaa): ")
    detalles_evento['lugar'] = input("Ingrese el lugar del evento: ")
    detalles_evento['asistentes'] = input("Ingrese el número de asistentes esperados: ")
    return detalles_evento

def validar_detalles_evento(detalles_evento):
    if not detalles_evento['nombre'] or not detalles_evento['fecha'] or not detalles_evento['lugar'] or not detalles_evento['asistentes']:
        return False
    return True

def guardar_evento(detalles_evento):
    pass