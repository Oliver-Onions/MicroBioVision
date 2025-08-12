
import sys

from PySide6.QtWidgets import QApplication

from view.main.mainframe import MainWindow

class GUInterface:
    
    def __init__(self):
        self.app = None
        self.mainWindow = None

    def start_gui(self):
        # Initialize the QApplication only once
        if self.app is None:
            self.app = QApplication(sys.argv)
            self.app.setStyle("Fusion")

        # Start the main window
        self.start_main_window()

        # Enter the Qt application loop
        sys.exit(self.app.exec())

    def start_main_window(self):
        
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def shutdown(self):
        if self.app:
            print("🧪 [GUInterface] Forcing application exit.")
            self.app.exit(0)
