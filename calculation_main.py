import sys
from calculation import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


class MyMainWindow(QMainWindow, Ui_Calcu):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)



    def MessBox(self):
        # 弹出MessageBox显示结果

        # a = int(self.lineEdit_a.text())
        # b = int(self.lineEdit_c.text())
        # result = a + b

        # result = self.lineEdit_2.text()
        # result = 'aaaa'
        self.checkText()

        result = self.calculator()

        QMessageBox.about(self, '结果', '%s' % result)

    def outPut(self):
        # 直接在输出框中显示结果

        self.checkText()
        result = self.calculator()
        # self.textEdit.setText(str(sum))
        self.lineEdit_d.setText(str(result))

    def checkText(self):
        # 检查所有输入是否存在
        if self.lineEdit_a.text() == self.lineEdit_d.text() or \
                self.lineEdit_b.text() == self.lineEdit_d.text() or \
                self.lineEdit_c.text() == self.lineEdit_d.text():
            QMessageBox.about(self, 'Input Error', '请重新输入数据！')

# 1. 检查输入是否正确的语句还有问题
# 2. 输入有问题，但是无法跳到重新输入步骤













    def calculator(self):
        a = int(self.lineEdit_a.text())
        b = int(self.lineEdit_c.text())

        if self.lineEdit_b.text() == '+':
            r = a + b
            return r
        elif self.lineEdit_b.text() == '-':
            r = a - b
            return r
        elif self.lineEdit_b.text() == '*':
            r = a * b
            return r
        elif self.lineEdit_b.text() == '/':
            r = a / b
            return r
        else:
            QMessageBox.warning(self, 'Error', '错误的运算符')
            self.lineEdit_d.setCursorPosition(0)
    def reset(self):
        # 清除所有数据，初始化
        self.lineEdit_a.clear()
        self.lineEdit_b.clear()
        self.lineEdit_c.clear()
        self.lineEdit_d.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWin = MyMainWindow()
    myWin.show()

    sys.exit(app.exec_())
