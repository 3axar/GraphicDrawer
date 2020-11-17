import sys
from PyQt5.QtWidgets import QApplication
from GraphicDrawerWindow import GraphicDrawerWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    graphic_drawer = GraphicDrawerWindow()

    sys.exit(app.exec_())
