# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculation.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calcu(object):
    def setupUi(self, Calcu):
        Calcu.setObjectName("Calcu")
        Calcu.resize(800, 800)
        Calcu.setMinimumSize(QtCore.QSize(800, 800))        # 设置窗口为固定大小
        Calcu.setMaximumSize(QtCore.QSize(800,800))          # 设置窗口为固定大小
        Calcu.setLayoutDirection(QtCore.Qt.LeftToRight)
        Calcu.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(Calcu)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(210, 40, 321, 31))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")



        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(180, 140, 111, 41))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_a.setAlignment(QtCore.Qt.AlignCenter)             #设置文本居中显示

        # ------------------------设置文本的字体-----------------------------------------------
        self.lineEdit_a.setStyleSheet("color:red")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(75)
        self.lineEdit_a.setFont(font)

        #------------------------密码模式-------------------------------------------------------------
        # self.lineEdit_a.setEchoMode(QtWidgets.QLineEdit.Password)



        #'''''''''''''''''''''''''''''''''运算符标签'''''''''''''''''''''''''''''''''''''''''''''''
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 120, 72, 15))
        self.label_2.setObjectName("label_2")

        #'''''''''''''''''''''''''''''''''运算符输入框'''''''''''''''''''''''''''''''''''''''''''''
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(330, 140, 70, 41))
        self.lineEdit_b.setObjectName("lineEdit_4")
        self.lineEdit_b.setAlignment(QtCore.Qt.AlignCenter)         #设置文本居中显示
        self.lineEdit_b.setFont(font)



        self.lineEdit_c = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c.setGeometry(QtCore.QRect(480, 140, 111, 41))
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.lineEdit_c.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_c.setFont(font)

        #'''''''''''''''''''''''''''''''''计算结果标签'''''''''''''''''''''''''''''''''''''''''''''''
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 280, 72, 15))
        self.label_3.setObjectName("label_3")

        # 计算结果输出在textEdit中
        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(320, 300, 111, 41))
        # self.textEdit.setObjectName("textEdit")

        self.lineEdit_d = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_d.setGeometry(QtCore.QRect(320, 300, 111, 41))
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.lineEdit_d.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_d.setFont(font)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(250, 430, 93, 51))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 430, 93, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 700, 93, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_1.clicked.connect(self.MessBox)
        self.pushButton_2.clicked.connect(self.outPut)
        self.pushButton_3.clicked.connect(self.reset)





        Calcu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calcu)
        self.statusbar.setObjectName("statusbar")
        Calcu.setStatusBar(self.statusbar)

        self.retranslateUi(Calcu)
        QtCore.QMetaObject.connectSlotsByName(Calcu)

    def retranslateUi(self, Calcu):
        _translate = QtCore.QCoreApplication.translate
        Calcu.setWindowTitle(_translate("Calcu", "计算器"))
        Calcu.setWhatsThis(_translate("Calcu", "这是什么"))
        Calcu.setAccessibleName(_translate("Calcu", "可访问的名字"))
        Calcu.setAccessibleDescription(_translate("Calcu", "可访问的描述"))
        Calcu.setWindowFilePath(_translate("Calcu", "文件路径"))

        self.label_1.setText(_translate("Calcu", "计算器"))

        self.lineEdit_a.setPlaceholderText(_translate("Calcu", "5"))
        # self.lineEdit_a.setText(_translate("Calcu", "0"))

        self.label_2.setText(_translate("Calcu", "运算符"))
        self.lineEdit_b.setPlaceholderText(_translate("Calcu", "+"))

        self.lineEdit_c.setPlaceholderText(_translate("Calcu", "8"))
        # self.lineEdit_c.setText(_translate("Calcu", "0"))

        self.label_3.setText(_translate("Calcu", "结果"))
        # 设置textEdit的值
        # self.textEdit.setPlaceholderText(_translate("Calcu", "3"))
        # self.textEdit.setText(_translate("Calcu", "22"))

        self.lineEdit_d.setPlaceholderText(_translate("Calcu", "8"))
        # self.lineEdit_d.setText(_translate("Calcu", "0"))

        self.pushButton_1.setText(_translate("Calcu", "计算"))
        self.pushButton_2.setText(_translate("Calcu", "计算并显示"))
        self.pushButton_3.setText(_translate("Calcu", "重置"))


