# SPDX-License-Identifier: MIT
"""
Reel Forge GUI - Application entry point.

Thin entry point that creates the QApplication and launches the
main window. All UI logic lives in src.app.ReelForgeApp.
"""

import sys
from PySide6.QtWidgets import QApplication
from src.app import ReelForgeApp


def main():
    """Create and run the Reel Forge GUI application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Reel Forge")
    window = ReelForgeApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
