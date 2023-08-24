from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication,QWidget
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Application")
        self.setWindowIcon(QIcon("slider\WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        # self.setFixedWidth(700)
        # self.setFixedHeight(700)
        self.setStyleSheet("background-color:green")
        self.setWindowOpacity(0.9)

app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())




ş







