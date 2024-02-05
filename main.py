from PySide6.QtWidgets import QApplication
from src.mainWindow import mainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow(app)
    window.show()
    app.exec()