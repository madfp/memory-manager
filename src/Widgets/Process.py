from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel
from PySide6.QtCore import QTimer
import psutil

class ProcessMonitorWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Creating - Deleting processes 
        self.createdProcess = []
        self.loadUI()

    def loadUI(self):
        # Vertical box container
        self.layout = QVBoxLayout(self) 
        # Showing the existing processes
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_content)
        self.scroll_area.setWidget(self.scroll_area_content)
        self.layout.addWidget(self.scroll_area)
        # Add the scroll to the main window
        self.setLayout(self.layout)
        self.update_processes()

    """ Updating existing processes """
    def update_processes(self):
        # Clear existing process labels
        for i in reversed(range(self.scroll_area_layout.count())):
            self.scroll_area_layout.itemAt(i).widget().setParent(None)

        # Get list of running processes
        processes = psutil.process_iter(['pid', 'name', 'username'])
        
        # Create labels for each process and add them to the layout
        for process in processes:
            process_label = QLabel(f"PID: {process.info['pid']} | Name: {process.info['name']} | Username: {process.info['username']}")
            self.scroll_area_layout.addWidget(process_label)     
        QTimer.singleShot(5000, self.update_processes)