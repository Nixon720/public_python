import sys
from PyQt5 import QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQt Tuts")
        self.setWindowIcon(QtGui.QIcon('pngegg.png'))
        self.show()

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())