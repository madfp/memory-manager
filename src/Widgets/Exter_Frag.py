"""
Ocurre cuando hay memoria libre disponible en el sistema, pero no hay una sola partición lo suficientemente grande como para alojar un proceso. Esto se produce cuando la memoria libre se divide en pequeños bloques que no son lo suficientemente grandes para los procesos que esperan ser ejecutados.

Puede resolverse mediante paginación, compactación y segmentación, por lo que la memoria se puede asignar a un programa de manera no contigua.

Simulacion:
1. Crea una lista que represente la memoria del sistema, donde cada elemento representa un bloque de memoria de tamaño fijo.
2. Crea una lista que represente los procesos que esperan ser ejecutados, donde cada elemento indica el tamaño de memoria que necesita el proceso.
3. Inicializa una variable para la memoria libre total.
4. Recorre la lista de procesos. Para cada proceso:
  - Si la memoria libre total es menor que el tamaño del proceso, aumenta la variable de fragmentación externa.
  - Si la memoria libre total es mayor o igual que el tamaño del proceso, reduce la memoria libre total en el tamaño del proceso.
  - Imprime el valor de la variable de fragmentación externa.
"""
from PySide6.QtWidgets import QWidget

class ExternFragmentation(QWidget):
  def __init__():
    super().__init__()
    # Atributes

  # Methods
    
"""
memoria = [100, 200, 300, 400, 500]
procesos = [120, 150, 250, 350, 450]

fragmentacion_externa = 0

memoria_libre = sum(memoria)

for proceso in procesos:
    if memoria_libre < proceso:
        fragmentacion_externa += proceso
    else:
        memoria_libre -= proceso

print("Fragmentación externa:", fragmentacion_externa)
"""
