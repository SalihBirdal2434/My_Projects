import typing
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QFont
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QMenu
import sys

class classwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,200,500,500)
        self.setWindowTitle("Salih's Python Program")
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.create_button()
    def create_button(self):
        button=QPushButton("Click",self)
        button.setGeometry(100,100,130,130)
        button.setFont(QFont("Times",14,QFont.Weight.ExtraBold))
        button.setIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        button.setIconSize(QSize(36,36))
        
        
        #popup menu 
        menu=QMenu()
        menu.addAction("Copy")
        menu.setFont(QFont("Times",14,QFont.Weight.ExtraBold))
        menu.setStyleSheet("background-color:green")
        menu.addAction("Cut")
        menu.addAction("Paste")
        button.setMenu(menu)
            
    
    
    
    
    
app=QApplication(sys.argv)
window=classwindow()
window.show()
sys.exit(app.exec())























































