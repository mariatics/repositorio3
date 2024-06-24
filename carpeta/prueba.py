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
print("Frecuencia absoluta:")
for valor, f in resultado.items():
        print(f"Valor {valor}: {f}")