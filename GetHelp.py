from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QTextEdit, QMainWindow, QDialog, QPushButton, QWidget
import PyQt5.QtWidgets


# for i in range(1, 10):
#
#     print(exec('t%d=1' % i))

# a = ['1', '2', '3', '0', '0']
# b = ['3', '4', '5']
# c = [a, b]
# d = [int(x) for x in a]
# print(c)
# print(d)

class Test():
    def __init__(self):
        self.a = 2
        self.b = 3

    def change(self):
        self.a = 3
        self.b = 5
        c = self.a + self.b
        print(c)


c = Test()
c.change()
