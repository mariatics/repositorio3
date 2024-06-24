
from clases import Clases

def frecuencia(Frec):
    frecuencia_acum = {}
    for valor in Frec:
        if valor in frecuencia_acum:
            frecuencia_acum[valor] += 1
        else:
            frecuencia_acum[valor] = 1
    return frecuencia_acum



from clases import Clases
from clases_ordenadas import clases_ordenadas
from frecuencia import frecuencia

    # Sección 1: Mostrar Clases
print("Clases:")
print(Clases)
print()

    # Sección 2: Clases ordenadas
Clases_ordenadas = clases_ordenadas(Clases)
print("Clases ordenadas:")
print(Clases_ordenadas)
print()

    # Sección 3: Frecuencia absoluta
resultado = frecuencia(Clases_ordenadas)
print("Frecuencia acum:")
for valor, f in resultado.items():
        print(f"Valor {valor}: {f}")