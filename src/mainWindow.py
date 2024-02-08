from PySide6.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QToolBar, QPushButton, QMessageBox
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QSize
from .Tabs import Widget
class mainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        # Window properties
        self.setWindowTitle("Task manager")
        self.setWindowIcon(QIcon("./icons/cpu.png"))
        self.setFixedSize(800, 550)
        self.app = app

        # Create de menubar
        menubar = self.menuBar()
        
        """ Settings Actions"""
        settings = menubar.addMenu("Settings")
        # Quit
        quit = settings.addAction("Quit")
        quit.triggered.connect(self.quitWindow)
        
        """ Help Actions"""
        help = menubar.addMenu("Help")
        # More information
        more_info = help.addAction("More information")
        more_info.triggered.connect(self.helpWindow)

        # Create the tab widget
        self.tab_widget = Widget()
        self.setCentralWidget(self.tab_widget)

        # Create the status bar
        self.setStatusBar(QStatusBar(self))
        # self.statusbar().showmessage("message", timeout-miliseconds)
    
    def Action1(self):
        print("Action1 triggered")

    def quitWindow(self):
        self.app.quit()

    def helpWindow(self):
        ret = QMessageBox.about(self, "How it works?", 
                                      "This application allows you to manage memory, processes and threads. Monitor memory usage in real time. View, filter and terminate processes, create new ones and master threads.")