from PySide6.QtWidgets import QMainWindow, QTabWidget
from PySide6.QtGui import QIcon
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window properties
        self.setWindowTitle("Task manager")
        self.setWindowIcon(QIcon("./icons/cpu.png"))
        self.setFixedSize(800, 500)

        # Create the tab widget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Add toolbar buttons
        #self.add_toolbar_button("Memory", "path/to/icon1.png", self.button1_clicked)
        #self.add_toolbar_button("Threads", "path/to/icon2.png", self.button2_clicked)
        #self.add_toolbar_button("Process", "path/to/icon3.png", self.button3_clicked)

    def add_toolbar_button(self, text, icon_path, callback):
        button = self.toolbar.addAction(QIcon(icon_path), text)
        button.triggered.connect(callback)

    def button1_clicked(self):
        print("Button 1 clicked!")

    def button2_clicked(self):
        print("Button 2 clicked!")

    def button3_clicked(self):
        print("Button 3 clicked!")