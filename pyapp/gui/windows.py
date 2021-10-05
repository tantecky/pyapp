from PySide6.QtWidgets import QMainWindow  # type: ignore

from pyapp import __version__


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"pyapp {__version__}")
        self.resize(1024, 768)
