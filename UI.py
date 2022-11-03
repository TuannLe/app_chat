from PyQt5 import uic, QtWidgets, QtCore 
from PyQt5.QtWidgets import QWidget, QApplication
import sys

class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('DoAn\\app_chat\\UI.ui', self) 
        self.show() 

app = QApplication(sys.argv)
window = Ui() 
app.exec_() 