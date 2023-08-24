from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu,QLineEdit,QHBoxLayout
from PyQt6.QtCore import QSize
import sys

class appwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 700, 700)
        self.setWindowTitle("Salih Birdal")
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.label()  # label
        self.create_button()  # button
        self.create_menu()  # menu
        self.line_example()
        self.hboxlayout()
        
        
        
    def label(self):
        label = QLabel("Python Development /Copyright Salih", self)
        label.move(500,500)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet("color:red")

    def create_button(self):
        self.button = QPushButton("Click", self)  # Store the button in an instance variable
        self.button.setGeometry(100, 100, 100, 100)
        self.button.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        self.button.setIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        self.button.setIconSize(QSize(36, 36))

    def create_menu(self):
        menu = QMenu(self)
        menu.addAction("Copy")
        menu.addAction("Paste")
        menu.addAction("Cut")
        menu.setStyleSheet("background-color:green")
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        self.button.setMenu(menu)
        
        
    def line_example(self):
        qline_edit=QLineEdit(self)
        qline_edit.setWindowTitle("Salih")
        qline_edit.setPlaceholderText("Şifrenizi girin...")
        qline_edit.setEchoMode(QLineEdit.EchoMode.Password)
        qline_edit.setGeometry(206,150,150,36)
        
        
    def hboxlayout(self):
        layout=QHBoxLayout()
        bt1=QPushButton("Click One")
        bt2=QPushButton("Click two")
        bt3=QPushButton("Click three")
        layout.addWidget(bt1)
        layout.addWidget(bt2)
        layout.addWidget(bt3)
        layout.addSpacing(300)
        self.setLayout(layout)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = appwindow()
    window.show()
    sys.exit(app.exec())



























































