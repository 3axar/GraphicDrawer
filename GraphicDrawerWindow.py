from PyQt5 import QtWidgets
from GraphicDrawer2 import Ui_MainWindow
from PlotCanvas import MyDynamicMplCanvas
from PlotCanvas import MyStaticMplCanvas
from PlotCanvas import ControllableMplCanvas
from numpy import random


class GraphicDrawerWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        l = QtWidgets.QVBoxLayout(self.widget)
        # sc = MyStaticMplCanvas(self.widget, width=5, height=4, dpi=100)
        # dc = MyDynamicMplCanvas(self.widget, width=5, height=4, dpi=100)
        self.hc = ControllableMplCanvas(self.widget, width=5, height=4, dpi=100)
        #l.addWidget(sc)
        #l.addWidget(dc)
        l.addWidget(self.hc)
        self.radioButton.clicked.connect(self.update_graph)

    def update_graph(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        x = [0, 1, 2, 3]
        y = [random.randint(0, 10) for i in range(4)]
        self.hc.update_figure(x, y)
