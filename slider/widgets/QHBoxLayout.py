from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu,QLineEdit,QHBoxLayout
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Salih's Program")
        self.setGeometry(200,200,400,700)
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.bush_button()
        
    def bush_button(self):
        hbox=QHBoxLayout()
        btn1=QPushButton("Click One")
        btn2=QPushButton("Click two")
        btn3=QPushButton("Click three")
        btn4=QPushButton("Click four")
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addStretch(10)
        self.setLayout(hbox)
    
        
        
        
        
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())











