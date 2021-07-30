# Author: Emil
# Description: Calculator GUI
# Based off of https://www.geeksforgeeks.org/building-calculator-using-pyqt5-in-python/


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle("Calculator ")

        # geometry of window, parameters are (x,y,width,height)
        self.setGeometry(500, 500, 360, 350)
        self.Build()
        self.show()
  
        # function to build all our widgets
    def Build(self):

        self.label = QLabel(self)
        self.label.setFont(QFont('Helvetica', 15))
        self.label.setWordWrap(True)
        # makes sure our label's text start at the right
        self.label.setAlignment(Qt.AlignRight)
        # style sheet for our qlabel
        self.label.setStyleSheet("QLabel {border:4px black; background:white;}")
        self.label.setGeometry(5, 15, 350, 70)
        

        # adding all of our number buttons and positioning them
        push0 = QPushButton("0", self)
        push0.clicked.connect(self.action0) #ties our button being clicked to function
        push0.setGeometry(5, 300, 80, 40)

        push1 = QPushButton("1", self)
        push1.clicked.connect(self.action1)
        push1.setGeometry(5, 150, 80, 40)

            
        push2 = QPushButton("2", self)
        push2.clicked.connect(self.action2)
        push2.setGeometry(95, 150, 80, 40)
                    
        push3 = QPushButton("3", self)
        push3.clicked.connect(self.action3)
        push3.setGeometry(185, 150, 80, 40)
  
        push4 = QPushButton("4", self)
        push4.clicked.connect(self.action4)
        push4.setGeometry(5, 200, 80, 40)
  
        push5 = QPushButton("5", self)
        push5.clicked.connect(self.action5)
        push5.setGeometry(95, 200, 80, 40)
  
        push6 = QPushButton("6", self)
        push6.clicked.connect(self.action6)
        push6.setGeometry(185, 200, 80, 40)
  
        push7 = QPushButton("7", self)
        push7.clicked.connect(self.action7)
        push7.setGeometry(5, 250, 80, 40)
  
        push8 = QPushButton("8", self)
        push8.clicked.connect(self.action8)
        push8.setGeometry(95, 250, 80, 40)
  
        push9 = QPushButton("9", self)
        push9.clicked.connect(self.action9)
        push9.setGeometry(185, 250, 80, 40)

        # adding our operator buttons now ===========
        push_plus = QPushButton("+", self) #addition
        push_plus.clicked.connect(self.action_plus)
        push_plus.setGeometry(275, 250, 80, 40)
  
        push_minus = QPushButton("-", self)#substraction
        push_minus.clicked.connect(self.action_minus)
        push_minus.setGeometry(275, 200, 80, 40)
  
        push_mul = QPushButton("*", self)#multiplication
        push_mul.clicked.connect(self.action_mul)
        push_mul.setGeometry(275, 150, 80, 40)
  
        push_div = QPushButton("/", self)#division
        push_div.clicked.connect(self.action_div)
        push_div.setGeometry(185, 300, 80, 40)

        push_power = QPushButton("^", self)#power
        push_power.clicked.connect(self.action_power)
        push_power.setGeometry(275, 100, 80, 40)
  
        push_point = QPushButton(".", self)#to add a decimal
        push_point.clicked.connect(self.action_point)
        push_point.setGeometry(95, 300, 80, 40)

        push_equal = QPushButton("=", self) #button to solve problem
        push_equal.clicked.connect(self.action_equal)
        # giving our equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
        push_equal.setGeometry(275, 300, 80, 40)
  
        push_clear = QPushButton("Clear", self)#to clear our text field
        push_clear.clicked.connect(self.action_clear)
        c_effect.setColor(Qt.red)
        push_clear.setGraphicsEffect(c_effect)
        push_clear.setGeometry(5, 100, 140, 40)
  
        push_del = QPushButton("Del", self)#to delete one number from our text field
        push_del.clicked.connect(self.action_del)
        c_effect.setColor(Qt.red)
        push_del.setGraphicsEffect(c_effect)
        push_del.setGeometry(150, 100, 115, 40)
  
    def action_equal(self):
  
        # get the label text
        equation = self.label.text()
  
        try:
            # getting the ans
            ans = eval(equation)
  
            # setting text to the label
            self.label.setText(str(ans))
  
        except:
            # setting text to the label
            self.label.setText("Wrong Input")
  
    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")
  
    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")
  
    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")
    
    def action_power(self):
        text = self.label.text()
        self.label.setText(text + " ^ ")
  
    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")
  
    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")

    def action_neg(self):
        text = self.label.text()
        self.label.setText(text + " -")
  
    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
  
    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
  
    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
  
    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
  
    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
  
    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
  
    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
  
    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
  
    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
  
    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
  
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
  
    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
