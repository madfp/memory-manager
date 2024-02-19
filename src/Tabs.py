from .Widgets.Process import ProcessMonitorWidget
from .Widgets.Memory import MemoriMonitorWidget
from .Widgets.ProcessSimulator import MemorySimulator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget(self)

        """ MEMORY CHART TAB """
        widget_memory = MemoriMonitorWidget()

        """ SIMULATOR """
        widget_simulator = MemorySimulator()
        
        """ PROCESSES TAB """
        widget_processes = ProcessMonitorWidget()

        #Add tabs to widget
        tab_widget.addTab(widget_memory,"Memory")
        tab_widget.addTab(widget_processes,"System processes")
        tab_widget.addTab(widget_simulator,"Simulator")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)