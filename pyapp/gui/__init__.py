from PySide6.QtWidgets import QApplication  # type: ignore

from pyapp.gui.windows import MainWindow


def show():
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
