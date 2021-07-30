#Author: Emil Roy
#Description: Program that'll allow you to enter any website link, and displays the QR code.

import pyqrcode 
from pyqrcode import QRCode

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QWidget
)

class QR_Generator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(1400, 800, 800, 700)

        self.layout = QGridLayout()
        button = QPushButton('->')
        self.textfield = QLineEdit(self)

        self.layout.addWidget(QLabel("Enter Link Here: "), 0, 0)
        self.layout.addWidget(self.textfield, 0, 1)
        self.layout.addWidget(button, 0, 2)
        button.clicked.connect(self.on_pushed)
        self.setLayout(self.layout)

    def on_pushed(self):
        link = self.textfield.text()

        # Generate QR code 
        url = pyqrcode.create(link)
  
        # Create and save the png file
        url.png("websiteQR.png", scale = 8)
        
        #create QLabel to hold our picture and display it on the window
        self.qrLabel = QLabel(self)
        self.pixmap = QPixmap('websiteQR.png')
        self.qrLabel.setPixmap(self.pixmap)
        
        self.layout.addWidget(self.qrLabel, 1, 1) #adds our picture to our grid layout
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QR_Generator()
    window.show()
    sys.exit(app.exec_())
  
 
