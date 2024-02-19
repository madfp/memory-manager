from PySide6 import QtWidgets, QtCore
import psutil
import random


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
        self.fix_problems = QtWidgets.QPushButton("Fix memory problems", self)
        self.delete_finished = QtWidgets.QPushButton("Delete finished processes", self)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_finished)
        self.layout.addWidget(self.fix_problems)
        self.setLayout(self.layout)

        # Funcionalidad
        self.add_button.clicked.connect(self.agregar_proceso)
        self.delete_finished.clicked.connect(self.cleanFinished)

        # Actualizar contenido
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
        self.processes.append(process)
        process_label = QtWidgets.QLabel(f"PID: {process.PID} | Required memory: {process.memoria}Mb | State: Nuevo | Assigned memory: {memoryBlock}Mb")
        self.scroll_area_layout.addWidget(process_label)
        self.allocatedMemory += memory

        # Validar si hay memoria disponible o queda espacio para un nuevo proceso
        if self.allocatedMemory >= (self.SystemMemory.available / 1024 ** 2) or memory+self.allocatedMemory > (self.SystemMemory.available / 1024 ** 2):
            # Mostrar un mensaje de error
            self.showError()
            return
        
        print(f"Used memory: {self.allocatedMemory}Mb - Available memory: {self.SystemMemory.available/ 1024 ** 2}Mb")

        # Agregar el proceso a la lista
        

        # Aplicar la técnica de gestión de memoria
        # ...

    # Implementar las técnicas de gestión de memoria
    # ...
        
    def showError(self):
        ret = QtWidgets.QMessageBox.critical(self,"There is no space available...",
                                        "This new process is going to be suspended until there is free space...",
                                        QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if ret == QtWidgets.QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    # Delete only the registry of the finished processes
    def cleanFinished(self):
        for i in reversed(range(self.scroll_area_layout.count())):
            if (self.processes[i].estado == "Terminado"):
              self.scroll_area_layout.itemAt(i).widget().setParent(None)
              self.processes.pop(i)
    
    # Update the view from all the processes
    def updateState(self):
        # Clear existing process labels
        for i in reversed(range(self.scroll_area_layout.count())):
            self.scroll_area_layout.itemAt(i).widget().setParent(None)

        # change state and write the processes
        for i in self.processes:
            i.changeState()
            if (i.estado == "Terminado"):
                self.allocatedMemory -= i.memoria
            process_label = QtWidgets.QLabel(f"PID: {i.PID} | Memory Req: {i.memoria} Mb | State: {i.estado} | Assigned memory: {i.bloque}Mb")
            self.scroll_area_layout.addWidget(process_label)
        # Timer to repeat the function
        QtCore.QTimer.singleShot(5000, self.updateState)

# Class process
class Process():
    def __init__(self, pid, memoria, bloque):
      self.PID = pid
      self.memoria = memoria
      self.bloque = bloque
      self.estado = ""

    # Modify the state from the process
    def changeState(self):
        # Actualizar el estado del proceso
        if (self.estado != "Terminado"):
            self.estado = random.choice(["Nuevo", "Nuevo bloqueado", "Suspendido", "Terminado"])