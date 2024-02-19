from PySide6 import QtWidgets, QtCore
import psutil
import random
import math 

class MemorySimulator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.processes = []
        # .total .used .free .available .percent
        self.SystemMemory = psutil.virtual_memory()
        self.allocatedMemory = 0
        self.init_ui()

    def init_ui(self):
        # Vertical box container
        self.layout = QtWidgets.QVBoxLayout(self) 
        # Section for showing the processes
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QtWidgets.QWidget()
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scroll_area_content)
        self.scroll_area.setWidget(self.scroll_area_content)
        self.add_button = QtWidgets.QPushButton("Add new process", self)
        self.delete_finished = QtWidgets.QPushButton("Clear finished processes", self)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_finished)
        self.setLayout(self.layout)

        # Connect buttons functionalities
        self.add_button.clicked.connect(self.agregar_proceso)
        self.delete_finished.clicked.connect(self.cleanFinished)

        # Update processes status
        self.updateState()

    def agregar_proceso(self):
        # Generar un nuevo proceso
        pid = random.randint(1000, 9999)
        memory = random.randint(100, 500)
        # Validate that the memory block is greater than the memory req
        memoryBlock = random.randint(100, 500)
        while memoryBlock < memory:
            memoryBlock = random.randint(100, 500)
        # Crear una nueva instancia de la clase proceso y almacenarlo en la lista de procesos
        process = Process(pid, memory, memoryBlock)        

        # Validar si hay memoria disponible o queda espacio para un nuevo proceso
        if self.allocatedMemory >= (self.SystemMemory.available / 1024 ** 2) or memory+self.allocatedMemory > (self.SystemMemory.available / 1024 ** 2):
            # Mostrar un mensaje de error
            self.showError(process)
            return
        else:
            # Add the process to the list
            self.processes.append(process)
            process_label = QtWidgets.QLabel(f"PID: {process.PID} | Required memory: {process.memory}Mb | State: Nuevo | Assigned memory: {process.block}Mb")
            self.scroll_area_layout.addWidget(process_label)
            self.allocatedMemory += memory
            #print(f"Used memory: {self.allocatedMemory}Mb - Available memory: {self.SystemMemory.available/ 1024 ** 2}Mb")

    # Aplicar las técnicas de gestión de memoria
    def detect_memory_leaks(self, process):
        if process.status != "Terminado" and process.optimized < 2:
            # Calcular la diferencia entre los dos valores
            diferencia = process.block - process.memory
            # Reducir el valor2 en la mitad de la diferencia
            valor2_reducido = process.block - diferencia / 2
            process.block = math.ceil(valor2_reducido)
            process.optimized += 1
            print(f"Required: {process.memory} - Assigned: {process.block}")
        

    # Error - no more free space    
    def showError(self, process):
        ret = QtWidgets.QMessageBox.critical(self,"There is no space available...",
                                        "This new process is going to be suspended until there is free space...",
                                        QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if ret == QtWidgets.QMessageBox.Ok : 
            # Add the process to the list
            self.processes.append(process)
            process_label = QtWidgets.QLabel(f"PID: {process.PID} | Required memory: {process.memory}Mb | State: Nuevo bloqueado | Assigned memory: {process.block}Mb")
            self.scroll_area_layout.addWidget(process_label)
            self.allocatedMemory += process.memory

    # Delete only the registry of the finished processes
    def cleanFinished(self):
        for i in reversed(range(self.scroll_area_layout.count())):
            if (self.processes[i].status == "Terminado"):
              self.scroll_area_layout.itemAt(i).widget().setParent(None)
              self.processes.pop(i)
    
    # Update the view from all the processes
    def updateState(self):
        # Clear existing process labels
        for i in reversed(range(self.scroll_area_layout.count())):
            self.scroll_area_layout.itemAt(i).widget().setParent(None)

        # change state and write the processes
        for i in self.processes:
            # Optimizar la memoria asignada
            self.detect_memory_leaks(i)
            # Cambiar el estado del proceso
            i.changeState()
            # Liberar la memoria cuando el proceso haya terminado
            if (i.status == "Terminado"):
                self.allocatedMemory -= i.memory
            process_label = QtWidgets.QLabel(f"PID: {i.PID} | Memory Req: {i.memory} Mb | State: {i.status} | Assigned memory: {i.block}Mb")
            self.scroll_area_layout.addWidget(process_label)
        # Timer to repeat the function
        QtCore.QTimer.singleShot(5000, self.updateState)

# Class process
class Process():
    def __init__(self, pid, memory, block):
      self.PID = pid
      self.memory = memory
      self.block = block
      self.status = ""
      self.optimized = 0

    # Modify the state from the process
    def changeState(self):
        # Actualizar el estado del proceso
        if (self.status != "Terminado"):
            self.status = random.choice(["Nuevo", "Nuevo bloqueado", "Suspendido", "Terminado"])