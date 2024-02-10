"""
Ocurre cuando una partición de memoria asignada a un proceso no se utiliza completamente. Esto significa que hay espacio libre dentro de la partición que no puede ser utilizado por otros procesos. La fragmentación interna se produce cuando el tamaño de la partición es mayor que el tamaño del proceso que se le asigna.

Puede solucionarse asignando memoria a los programas en porciones dinámicas de bloques de memoria a su gusto y liberándola cuando no la necesite durante la ejecución de un programa.

Simulacion:
1. Crea una lista que represente la memoria del sistema, donde cada elemento representa un bloque de memoria de tamaño fijo.
2. Crea una lista que represente los procesos que esperan ser ejecutados, donde cada elemento indica el tamaño de memoria que necesita el proceso.
3. Recorre la lista de procesos. Para cada proceso:
  - Busca un bloque de memoria en la lista de memoria que sea lo suficientemente grande como para alojar el proceso.
  - Si se encuentra un bloque de memoria adecuado, asigna el proceso al bloque y actualiza la lista de memoria.
  - Si no se encuentra un bloque de memoria adecuado, aumenta la variable de fragmentación interna.
  - Imprime el valor de la variable de fragmentación interna.
"""
from PySide6.QtWidgets import QWidget

class InternFragmentation(QWidget):
  def __init__(self):
    super().__init__()
    self.availableMemory = []
    self.processes = []
    # atributes

  #methods
    
"""    
memoria = [100, 200, 300, 400, 500]
procesos = [120, 150, 250, 350]

fragmentacion_interna = 0

for proceso in procesos:
    for bloque in memoria:
        if bloque >= proceso:
            memoria[memoria.index(bloque)] -= proceso
            break
    else:
        fragmentacion_interna += proceso

print("Fragmentación interna:", fragmentacion_interna) 
"""