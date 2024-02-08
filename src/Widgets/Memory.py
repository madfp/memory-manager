import psutil
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import QTimer
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget, QVBoxLayout

class MemoriMonitorWidget(QWidget):
    def __init__(self):
        super().__init__()
        ### Memory chart ###
        self.memoryFigure = Figure()
        self.memoryCanvas = FigureCanvas(self.memoryFigure)
        self.generalLayout = QVBoxLayout()
        self.generalLayout.addWidget(self.memoryCanvas)
        self.setLayout(self.generalLayout)
        self.update_chart()

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
        ax.bar(["Used", "Free", "Total"], [used_memory, free_memory, total_memory])
        ax.set_ylabel("Gigabytes")
        ax.set_xlabel("Category")
        ax.set_title("Memory stats")
        # Actualizar el gráfico
        self.memoryCanvas.draw()

        # Programar la próxima actualización en 1 segundo
        QTimer.singleShot(1000, self.update_chart)