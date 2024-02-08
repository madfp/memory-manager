from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton
from PySide6.QtCore import QTimer
import psutil
import random
import os

class ProcessMonitorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout() # Box container
        # Creating - Deleting processes 
        self.createdProcess = []
        self.create = QWidget()
        self.createProcess = QPushButton("Create random processes")
        self.createProcess.clicked.connect(self.createProcessFn)
        self.deleteProcess = QPushButton("Delete random processes")
        self.deleteProcess.clicked.connect(self.deleteProcessFn)
        self.layout.addWidget(self.createProcess)
        self.layout.addWidget(self.deleteProcess)
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
    
    """ Creating processes """
    def createProcessFn(self):
        num_proc = random.randint(1,10)
        for i in range(num_proc):
            Pid = random.randint(1000,9999)
            threads = random.randint(2020, 5555)
            self.createdProcess.append([Pid, threads]) 
    
    """ Deleting processes """
    def deleteProcessFn(self):        
        for i in self.createdProcess:
            self.createdProcess.remove(i)
        print(self.createdProcess)
        

    """ Updating existing processes """
    def update_processes(self):
        # Clear existing process labels
        for i in reversed(range(self.scroll_area_layout.count())):
            self.scroll_area_layout.itemAt(i).widget().setParent(None)

        # Get list of running processes
        processes = psutil.process_iter(['pid', 'name'])
        
        # Create labels for each process and add them to the layout
        for process in processes:
            process_label = QLabel(f"PID: {process.info['pid']} | Name: {process.info['name']}")
            self.scroll_area_layout.addWidget(process_label)     
        QTimer.singleShot(5000, self.update_processes)