from PySide6.QtWidgets import QMainWindow, QStatusBar, QMessageBox
from PySide6.QtGui import QIcon
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
        
        """ SETTINGS ACTIONS """
        settings = menubar.addMenu("Settings")
        # Quit
        quit = settings.addAction("Quit")
        quit.triggered.connect(self.quitWindow)
        
        """ HELP ACTIONS """
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

    def quitWindow(self):
        self.app.quit()

    def helpWindow(self):
        ret = QMessageBox.about(self, "How it works?", 
                                      "This application allows you to manage memory, processes and threads. Monitor memory usage in real time. View, filter and terminate processes, create new ones and master threads.")