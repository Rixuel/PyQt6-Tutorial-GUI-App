from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys, random

FontSize = 30

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.names = [
            "ABC",
            "DEF",
            "GHI",
            "JKL",
            "MNO"
            ]
        
        # Adding Widgets
        self.text = QLabel("Hello")
        self.text.setFont(QFont("Arial", FontSize))
        self.button = QPushButton("Push Button!")
        self.button.setFont(QFont("Verdana", 10, QFont.Weight.Bold))
        self.button.clicked.connect(self.changeText)

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.show()
        self.resize(500, 200)
        self.setWindowTitle("PyQt6 Tutorial GUI App")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.setStyleSheet("""
            background: #CCCCCC;
            color: #224466;
        """)

    def changeText(self):
        self.text.setText(random.choice(self.names))

app = QApplication([])

win = MainWindow()

sys.exit(app.exec())