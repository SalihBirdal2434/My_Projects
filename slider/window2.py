from PyQt6.QtWidgets import QApplication,QMainWindow

import sys


app=QApplication(sys.argv) #base app
 
window=QMainWindow()

window.statusBar().showMessage("Welcome to PyQt6 Course")
window.menuBar().addMenu("File")

window.show() #exxecute

sys.exit(app.exec())

