from .Widgets.Process import ProcessMonitorWidget
from.Widgets.Memory import MemoriMonitorWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget(self)

        """ MEMORY CHART TAB """
        widget_memory = MemoriMonitorWidget()

        """ INTERN MEMORY FRAGMENTATION """
        widget_intern_fragmentation = QWidget()

        """ EXTERN MEMORY FRAGMENTATION """
        widget_extern_fragmentation = QWidget()

        """ MEMORY SEGMENTATION """
        widget_segmentation = QWidget()

        """ PAGINATION """
        widget_pagination = QWidget()

        """ PROCESSES TAB """
        widget_processes = ProcessMonitorWidget()

        #Add tabs to widget
        tab_widget.addTab(widget_memory,"Memory")
        tab_widget.addTab(widget_intern_fragmentation, "Intern Fragmentation")
        tab_widget.addTab(widget_extern_fragmentation, "Extern Fragmentation")
        tab_widget.addTab(widget_segmentation, "Segmentation")
        tab_widget.addTab(widget_pagination, "Pagination")
        tab_widget.addTab(widget_processes,"Processes")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)