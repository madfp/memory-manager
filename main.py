from PySide6.QtWidgets import QApplication
from src.mainWindow import mainWindow
import sys

if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow(app)
    window.show()
    sys.exit(app.exec())