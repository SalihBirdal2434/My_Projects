from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu,QLineEdit,QHBoxLayout,QVBoxLayout
from PyQt6.QtCore import QSize
import sys

class appwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 700, 700)
        self.setWindowTitle("Salih Birdal")
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.creare_widget()
        self.cliked_btn()
        self.label=QLabel("Default Text")
        
        
    def creare_widget(self):
        hbox=QHBoxLayout()
        btn=QPushButton("Change Text")
        btn.clicked.connect(self.cliked_btn)
        self.label=QLabel("Default Text")
        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        
    
    def cliked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times",15))
        self.label.setStyleSheet("color:red")
        
        

     
     
     
        """
            vbox=QVBoxLayout()
            btn1=QPushButton("Click one")
            btn2=QPushButton("Click two")
            btn3=QPushButton("Click three")
        
            vbox.addWidget(btn1)
            vbox.addWidget(btn2)
            vbox.addWidget(btn3)
            
            self.setLayout(vbox)
        
        """
        
        
        
        
app = QApplication(sys.argv)
window = appwindow()
window.show()
sys.exit(app.exec())

        
        
        
        
        
        
        