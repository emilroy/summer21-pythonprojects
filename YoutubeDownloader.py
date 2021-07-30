#Author: Emil
#Description: GUI to allow user to input YouTube link in order for them to download it
#ISSUE: pytube returns 404 error which other users have experienced as well. waiting for fix for that one

from pytube import YouTube

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QWidget
)

class Downloader(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Video Downloader")

        layout = QGridLayout()
        self.download_progress = QLabel(self)
        button = QPushButton('->')
        self.textfield = QLineEdit(self)

        layout.addWidget(QLabel("Enter Link Here: "), 0, 0)
        layout.addWidget(self.textfield, 0, 1)
        layout.addWidget(button, 0, 2)
        layout.addWidget(self.download_progress, 1, 0)
        button.clicked.connect(self.on_pushed)
        self.setLayout(layout)

    def on_pushed(self):
        yt = YouTube(self.textfield.text())
        video = yt.streams.get_highest_resolution()
        download_progress.setText("Download In Progress.....")
        video.download()
        download_progress.setText("Download Complete!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Downloader()
    window.show()
    sys.exit(app.exec_())
