from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit,QSpacerItem, QLabel
import psutil
import sys
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget(self)

        """ GENERAL TAB """
        widget_general = QWidget() # Creating the general widget (general tab)
        ### Memory chart ###
        self.memoryFigure = Figure()
        self.memoryCanvas = FigureCanvas(self.memoryFigure)
        self.generalLayout = QVBoxLayout()
        self.generalLayout.addWidget(self.memoryCanvas)

        # Set the widgets in the general tab
        widget_general.setLayout(self.generalLayout)

        # Actualizar grafico de memoria
        self.update_chart()

        """ MEMORY TAB """
        widget_memory = QWidget()
        label_full_name = QLabel("Full name :")
        line_edit_full_name = QLineEdit()
        memory_layout = QHBoxLayout()
        memory_layout.addWidget(label_full_name)
        memory_layout.addWidget(line_edit_full_name)
        widget_memory.setLayout(memory_layout)

        """ THREADS TAB """
        widget_threads = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        threads_layout = QVBoxLayout()
        threads_layout.addWidget(button_1)
        threads_layout.addWidget(button_2)
        threads_layout.addWidget(button_3)
        widget_threads.setLayout(threads_layout)

        """ PROCESSES TAB """
        widget_processes = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        processes_layout = QVBoxLayout()
        processes_layout.addWidget(button_1)
        processes_layout.addWidget(button_2)
        processes_layout.addWidget(button_3)
        widget_processes.setLayout(processes_layout)

        #Add tabs to widget
        tab_widget.addTab(widget_general,"Memory")
        tab_widget.addTab(widget_memory,"CPU")
        tab_widget.addTab(widget_threads,"Handling memory")
        tab_widget.addTab(widget_processes,"Threads")
        tab_widget.addTab(widget_processes,"Processes")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def button_1_clicked(self):
        print("Button clicked")

    def update_chart(self):
        # Obtener los datos de la memoria RAM
        memory = psutil.virtual_memory()
        used_memory = memory.used / 1024 / 1024 / 1024
        free_memory = memory.available / 1024 / 1024 / 1024
        total_memory = memory.total / 1024 / 1024 / 1024

        # Limpiar el gráfico
        self.memoryFigure.clear()

        # Crear el gráfico de barras
        ax = self.memoryFigure.add_subplot(111)
        ax.bar(["Utilizada", "Libre", "Total"], [used_memory, free_memory, total_memory])

        # Actualizar el gráfico
        self.memoryCanvas.draw()

        # Programar la próxima actualización en 1 segundo
        QTimer.singleShot(1000, self.update_chart)

"""
fragmentación interna y externa, paginación, segmentación.
"""