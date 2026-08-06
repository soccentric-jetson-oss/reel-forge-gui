"""Reel Forge GUI - Entry point."""
import sys
from PySide6.QtWidgets import QApplication
from src.app import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Reel Forge")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
