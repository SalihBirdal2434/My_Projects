from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu,QLineEdit
from PyQt6.QtCore import QSize
import sys

class appwindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Salih Programming")
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.setGeometry(700,200,300,600)
        linEdit=QLineEdit(self)
        linEdit.setFont(QFont("Sanerif",15))
        #linEdit.setText("Default Text")
        linEdit.setPlaceholderText("Please enter your username")
        # linEdit.setEnabled(False)
        linEdit.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        
        
        
        
        
        
        
        
app=QApplication(sys.argv)
window=appwindow()
window.show()
sys.exit(app.exec())










































