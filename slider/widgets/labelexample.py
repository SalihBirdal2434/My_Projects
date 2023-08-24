from PyQt6.QtGui import QIcon,QFont,QPixmap,QMovie
from PyQt6.QtWidgets import QApplication,QWidget,QLabel
import sys


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Salih Programming")
        self.setWindowIcon(QIcon("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg"))
        """
        label=QLabel("Python Development /Copright=salih",self)
        #label.setText("New text is here")
        label.move(100,100)
        label.setFont(QFont("Sanserif",15))
        label.setStyleSheet("color:red")
        label.setText(str(12))
        label.setNum(15)
        """
        """
        label=QLabel(self)
        pixmap=QPixmap("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg")
        label.setPixmap(pixmap)
        """
        
        label=QLabel(self)
        movie=QMovie("slider/WhatsApp Image 2022-08-26 at 20.46.37.jpeg")
        
        label.setMovie(movie)
        movie.start()
        





        
app=QApplication(sys.argv)
classwindow=window()
classwindow.show()
sys.exit(app.exec())

        










































































































