"""
La segmentación divide la memoria en segmentos de tamaño variable, cada uno con un propósito específico. Los segmentos pueden ser de código, datos, pila, etc. Los programas pueden acceder a los segmentos de memoria mediante una tabla de segmentos que contiene la dirección de inicio y el tamaño de cada segmento.

1. Crea una lista que represente la memoria del sistema, donde cada elemento representa un bloque de memoria de tamaño fijo.
2. Crea una lista que represente los segmentos de memoria que se han asignado a los procesos. Cada segmento debe tener información sobre el tamaño del segmento, la dirección de inicio y el proceso al que pertenece.
3. Recorre la lista de segmentos. Para cada segmento:
4. Busca un bloque de memoria en la lista de memoria que sea lo suficientemente grande como para alojar el segmento.
5. Si se encuentra un bloque de memoria adecuado, asigna el segmento al bloque y actualiza la lista de memoria.
6. Si no se encuentra un bloque de memoria adecuado, el sistema operativo debe buscar otro lugar en la memoria para alojar el segmento.
7. Imprime la lista de segmentos y la lista de memoria.
"""
from PySide6.QtWidgets import QWidget

class Segmentation(QWidget):
  def __init__():
    super().__init__()
    # atributes

  #methods
    
"""
memoria = [100, 200, 300, 400, 500]
segmentos = [
    {"proceso": "A", "tamaño": 120, "direccion_inicio": 0},
    {"proceso": "B", "tamaño": 150, "direccion_inicio": 120},
    {"proceso": "C", "tamaño": 250, "direccion_inicio": 270},
]

for segmento in segmentos:
    for bloque in memoria:
        if bloque >= segmento["tamaño"]:
            memoria[memoria.index(bloque)] -= segmento["tamaño"]
            segmento["direccion_inicio"] = memoria.index(bloque) * 100
            break

print("Segmentos:", segmentos)
print("Memoria:", memoria)
"""