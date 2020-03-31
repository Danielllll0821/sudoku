import sys
import datetime
from solutionSudoku import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义每行输入数据组成一给列表
        self.row1 = [self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),
                     self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text(),
                     self.lineEdit_9.text()]
        self.row2 = [self.lineEdit_10.text(), self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text(),
                     self.lineEdit_14.text(), self.lineEdit_15.text(), self.lineEdit_16.text(), self.lineEdit_17.text(),
                     self.lineEdit_18.text()]
        self.row3 = [self.lineEdit_19.text(), self.lineEdit_20.text(), self.lineEdit_21.text(), self.lineEdit_22.text(),
                     self.lineEdit_23.text(), self.lineEdit_24.text(), self.lineEdit_25.text(), self.lineEdit_26.text(),
                     self.lineEdit_27.text()]
        self.row4 = [self.lineEdit_28.text(), self.lineEdit_29.text(), self.lineEdit_30.text(), self.lineEdit_31.text(),
                     self.lineEdit_32.text(), self.lineEdit_33.text(), self.lineEdit_34.text(), self.lineEdit_35.text(),
                     self.lineEdit_36.text()]
        self.row5 = [self.lineEdit_37.text(), self.lineEdit_38.text(), self.lineEdit_39.text(), self.lineEdit_40.text(),
                     self.lineEdit_41.text(), self.lineEdit_42.text(), self.lineEdit_43.text(), self.lineEdit_44.text(),
                     self.lineEdit_45.text()]
        self.row6 = [self.lineEdit_46.text(), self.lineEdit_47.text(), self.lineEdit_48.text(), self.lineEdit_49.text(),
                     self.lineEdit_50.text(), self.lineEdit_51.text(), self.lineEdit_52.text(), self.lineEdit_53.text(),
                     self.lineEdit_54.text()]
        self.row7 = [self.lineEdit_55.text(), self.lineEdit_56.text(), self.lineEdit_57.text(), self.lineEdit_58.text(),
                     self.lineEdit_59.text(), self.lineEdit_60.text(), self.lineEdit_61.text(), self.lineEdit_62.text(),
                     self.lineEdit_63.text()]
        self.row8 = [self.lineEdit_64.text(), self.lineEdit_65.text(), self.lineEdit_66.text(), self.lineEdit_67.text(),
                     self.lineEdit_68.text(), self.lineEdit_69.text(), self.lineEdit_70.text(), self.lineEdit_71.text(),
                     self.lineEdit_72.text()]
        self.row9 = [self.lineEdit_73.text(), self.lineEdit_74.text(), self.lineEdit_75.text(), self.lineEdit_76.text(),
                     self.lineEdit_77.text(), self.lineEdit_78.text(), self.lineEdit_79.text(), self.lineEdit_80.text(),
                     self.lineEdit_81.text()]



    def getLineEdit(self):
        # 从输入框中获得数据

        # 定义输入框每行为一列表
        row1 = [self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),
                self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text(),
                self.lineEdit_9.text()]
        row2 = [self.lineEdit_10.text(), self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text(),
                self.lineEdit_14.text(), self.lineEdit_15.text(), self.lineEdit_16.text(), self.lineEdit_17.text(),
                self.lineEdit_18.text()]
        row3 = [self.lineEdit_19.text(), self.lineEdit_20.text(), self.lineEdit_21.text(), self.lineEdit_22.text(),
                self.lineEdit_23.text(), self.lineEdit_24.text(), self.lineEdit_25.text(), self.lineEdit_26.text(),
                self.lineEdit_27.text()]
        row4 = [self.lineEdit_28.text(), self.lineEdit_29.text(), self.lineEdit_30.text(), self.lineEdit_31.text(),
                self.lineEdit_32.text(), self.lineEdit_33.text(), self.lineEdit_34.text(), self.lineEdit_35.text(),
                self.lineEdit_36.text()]
        row5 = [self.lineEdit_37.text(), self.lineEdit_38.text(), self.lineEdit_39.text(), self.lineEdit_40.text(),
                self.lineEdit_41.text(), self.lineEdit_42.text(), self.lineEdit_43.text(), self.lineEdit_44.text(),
                self.lineEdit_45.text()]
        row6 = [self.lineEdit_46.text(), self.lineEdit_47.text(), self.lineEdit_48.text(), self.lineEdit_49.text(),
                self.lineEdit_50.text(), self.lineEdit_51.text(), self.lineEdit_52.text(), self.lineEdit_53.text(),
                self.lineEdit_54.text()]
        row7 = [self.lineEdit_55.text(), self.lineEdit_56.text(), self.lineEdit_57.text(), self.lineEdit_58.text(),
                self.lineEdit_59.text(), self.lineEdit_60.text(), self.lineEdit_61.text(), self.lineEdit_62.text(),
                self.lineEdit_63.text()]
        row8 = [self.lineEdit_64.text(), self.lineEdit_65.text(), self.lineEdit_66.text(), self.lineEdit_67.text(),
                self.lineEdit_68.text(), self.lineEdit_69.text(), self.lineEdit_70.text(), self.lineEdit_71.text(),
                self.lineEdit_72.text()]
        row9 = [self.lineEdit_73.text(), self.lineEdit_74.text(), self.lineEdit_75.text(), self.lineEdit_76.text(),
                self.lineEdit_77.text(), self.lineEdit_78.text(), self.lineEdit_79.text(), self.lineEdit_80.text(),
                self.lineEdit_81.text()]
        # print(row1)
        # 将字符列表转为数字列表
        row1 = [int(x) for x in row1]
        row2 = [int(x) for x in row2]
        row3 = [int(x) for x in row3]
        row4 = [int(x) for x in row4]
        row5 = [int(x) for x in row5]
        row6 = [int(x) for x in row6]
        row7 = [int(x) for x in row7]
        row8 = [int(x) for x in row8]
        row9 = [int(x) for x in row9]
        rowAll = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
        return row1, row2, row3, row4, row5, row6, row7, row8, row9, rowAll

    def result(self):
        # 计算数独的结果

        # print('a')
        row1 = self.getLineEdit()[0]  # 从getLineEdit()函数中得到获得的数据.（初始输入数据列表）
        row2 = self.getLineEdit()[1]
        row3 = self.getLineEdit()[2]
        row4 = self.getLineEdit()[3]
        row5 = self.getLineEdit()[4]
        row6 = self.getLineEdit()[5]
        row7 = self.getLineEdit()[6]
        row8 = self.getLineEdit()[7]
        row9 = self.getLineEdit()[8]
        # print(row1)
        s = solution(self.getLineEdit()[9]).start()  # 通过获得的数据计算出数独的解，解是一个计算结果列表
        # print(s)
        # print(type(s))    #显示输出结果的类型
        # print(self.lineEdit_8.text())     #显示
        r1 = [str(x) for x in s[0]]  # 将计算结果（整数列表）的第一个元素作为数独的第一行,转换成字符串列表
        # print(r1)
        r2 = [str(x) for x in s[1]]
        r3 = [str(x) for x in s[2]]
        r4 = [str(x) for x in s[3]]
        r5 = [str(x) for x in s[4]]
        r6 = [str(x) for x in s[5]]
        r7 = [str(x) for x in s[6]]
        r8 = [str(x) for x in s[7]]
        r9 = [str(x) for x in s[8]]

        # 输入框的数据每行为一个列表，将该列表的索引和元素组成字典，以便下面通过索引确定元素
        d1 = {0: self.lineEdit_1, 1: self.lineEdit_2, 2: self.lineEdit_3, 3: self.lineEdit_4, 4: self.lineEdit_5,
              5: self.lineEdit_6, 6: self.lineEdit_7, 7: self.lineEdit_8, 8: self.lineEdit_9}
        d2 = {0: self.lineEdit_10, 1: self.lineEdit_11, 2: self.lineEdit_12, 3: self.lineEdit_13, 4: self.lineEdit_14,
              5: self.lineEdit_15, 6: self.lineEdit_16, 7: self.lineEdit_17, 8: self.lineEdit_18}
        d3 = {0: self.lineEdit_19, 1: self.lineEdit_20, 2: self.lineEdit_21, 3: self.lineEdit_22, 4: self.lineEdit_23,
              5: self.lineEdit_24, 6: self.lineEdit_25, 7: self.lineEdit_26, 8: self.lineEdit_27}
        d4 = {0: self.lineEdit_28, 1: self.lineEdit_29, 2: self.lineEdit_30, 3: self.lineEdit_31, 4: self.lineEdit_32,
              5: self.lineEdit_33, 6: self.lineEdit_34, 7: self.lineEdit_35, 8: self.lineEdit_36}
        d5 = {0: self.lineEdit_37, 1: self.lineEdit_38, 2: self.lineEdit_39, 3: self.lineEdit_40, 4: self.lineEdit_41,
              5: self.lineEdit_42, 6: self.lineEdit_43, 7: self.lineEdit_44, 8: self.lineEdit_45}
        d6 = {0: self.lineEdit_46, 1: self.lineEdit_47, 2: self.lineEdit_48, 3: self.lineEdit_49, 4: self.lineEdit_50,
              5: self.lineEdit_51, 6: self.lineEdit_52, 7: self.lineEdit_53, 8: self.lineEdit_54}
        d7 = {0: self.lineEdit_55, 1: self.lineEdit_56, 2: self.lineEdit_57, 3: self.lineEdit_58, 4: self.lineEdit_59,
              5: self.lineEdit_60, 6: self.lineEdit_61, 7: self.lineEdit_62, 8: self.lineEdit_63}
        d8 = {0: self.lineEdit_64, 1: self.lineEdit_65, 2: self.lineEdit_66, 3: self.lineEdit_67, 4: self.lineEdit_68,
              5: self.lineEdit_69, 6: self.lineEdit_70, 7: self.lineEdit_71, 8: self.lineEdit_72}
        d9 = {0: self.lineEdit_73, 1: self.lineEdit_74, 2: self.lineEdit_75, 3: self.lineEdit_76, 4: self.lineEdit_77,
              5: self.lineEdit_78, 6: self.lineEdit_79, 7: self.lineEdit_80, 8: self.lineEdit_81}

        # 对初始输入数据进行检查，为0的输入框，需要将结果写入进去
        for i in range(0, 9):  # i 代表行数据列表的索引
            # print(row1[i])
            if row1[i] == 0:  # 从输入框中获取的数据如果是0。row1是初始输入数据的列表
                newNum = r1[i]  # 将计算结果列表对应索引的元素赋值给要重新写入框中的数据。r1是计算结果列表
                d1[i].setStyleSheet("color:red")  # 由索引在字典中对应的键，获得字典的值，据此获得相应的lineEdit
                d1[i].setText(newNum)

        for i in range(0, 9):
            if row2[i] == 0:
                newNum = r2[i]
                d2[i].setStyleSheet("color:red")
                d2[i].setText(newNum)

        for i in range(0, 9):
            if row3[i] == 0:
                newNum = r3[i]
                d3[i].setStyleSheet("color:red")
                d3[i].setText(newNum)

        for i in range(0, 9):
            if row4[i] == 0:
                newNum = r4[i]
                d4[i].setStyleSheet("color:red")
                d4[i].setText(newNum)
        for i in range(0, 9):
            if row5[i] == 0:
                newNum = r5[i]
                d5[i].setStyleSheet("color:red")
                d5[i].setText(newNum)

            if row6[i] == 0:
                newNum = r6[i]
                d6[i].setStyleSheet("color:red")
                d6[i].setText(newNum)

        for i in range(0, 9):
            if row7[i] == 0:
                newNum = r7[i]
                d7[i].setStyleSheet("color:red")
                d7[i].setText(newNum)
        for i in range(0, 9):
            if row8[i] == 0:
                newNum = r8[i]
                d8[i].setStyleSheet("color:red")
                d8[i].setText(newNum)
        for i in range(0, 9):
            if row9[i] == 0:
                newNum = r9[i]
                d9[i].setStyleSheet("color:red")
                d9[i].setText(newNum)

    def reset(self):
        # for i in range(1,82):
        #     self.lineEdit_.clear()
        self.setupUi(self)


        # self.lineEdit_1.clear()
        #
        # self.lineEdit_1.setText('0')
        # self.lineEdit_2.setText('0')
        # self.lineEdit_3.setText('0')
        # self.lineEdit_4.setText('0')
        # self.lineEdit_5.setText('0')
        # self.lineEdit_6.setText('0')
        # self.lineEdit_7.setText('0')
        # self.lineEdit_8.setText('0')
        # self.lineEdit_9.setText('0')
        # self.lineEdit_10.setText('0')
        # self.lineEdit_11.setText('0')
        # self.lineEdit_12.setText('0')
        # self.lineEdit_13.setText('0')
        # self.lineEdit_14.setText('0')
        # self.lineEdit_15.setText('0')
        # self.lineEdit_16.setText('0')
        # self.lineEdit_17.setText('0')
        # self.lineEdit_18.setText('0')
        # self.lineEdit_19.setText('0')
        # self.lineEdit_20.setText('0')
        # self.lineEdit_21.setText('0')
        # self.lineEdit_22.setText('0')
        # self.lineEdit_23.setText('0')
        # self.lineEdit_24.setText('0')
        # self.lineEdit_25.setText('0')
        # self.lineEdit_26.setText('0')
        # self.lineEdit_27.setText('0')
        # self.lineEdit_28.setText('0')
        # self.lineEdit_29.setText('0')
        # self.lineEdit_30.setText('0')
        # self.lineEdit_31.setText('0')
        # self.lineEdit_32.setText('0')
        # self.lineEdit_33.setText('0')
        # self.lineEdit_34.setText('0')
        # self.lineEdit_35.setText('0')
        # self.lineEdit_36.setText('0')
        # self.lineEdit_37.setText('0')
        # self.lineEdit_38.setText('0')
        # self.lineEdit_39.setText('0')
        # self.lineEdit_40.setText('0')
        # self.lineEdit_41.setText('0')
        # self.lineEdit_42.setText('0')
        # self.lineEdit_43.setText('0')
        # self.lineEdit_44.setText('0')
        # self.lineEdit_45.setText('0')
        # self.lineEdit_46.setText('0')
        # self.lineEdit_47.setText('0')
        # self.lineEdit_48.setText('0')
        # self.lineEdit_49.setText('0')
        # self.lineEdit_50.setText('0')
        # self.lineEdit_51.setText('0')
        # self.lineEdit_52.setText('0')
        # self.lineEdit_53.setText('0')
        # self.lineEdit_54.setText('0')
        # self.lineEdit_55.setText('0')
        # self.lineEdit_56.setText('0')
        # self.lineEdit_57.setText('0')
        # self.lineEdit_58.setText('0')
        # self.lineEdit_59.setText('0')
        # self.lineEdit_60.setText('0')
        # self.lineEdit_61.setText('0')
        # self.lineEdit_62.setText('0')
        # self.lineEdit_63.setText('0')
        # self.lineEdit_64.setText('0')
        # self.lineEdit_65.setText('0')
        # self.lineEdit_66.setText('0')
        # self.lineEdit_67.setText('0')
        # self.lineEdit_68.setText('0')
        # self.lineEdit_69.setText('0')
        # self.lineEdit_70.setText('0')
        # self.lineEdit_71.setText('0')
        # self.lineEdit_72.setText('0')
        # self.lineEdit_73.setText('0')
        # self.lineEdit_74.setText('0')
        # self.lineEdit_75.setText('0')
        # self.lineEdit_76.setText('0')
        # self.lineEdit_77.setText('0')
        # self.lineEdit_78.setText('0')
        # self.lineEdit_79.setText('0')
        # self.lineEdit_80.setText('0')
        # self.lineEdit_81.setText('0')


class solution(object):
    def __init__(self, board):
        self.b = board
        self.t = 0

    def check(self, x, y, value):  # 检查每行每列及每宫是否有相同项
        for row_item in self.b[x]:
            if row_item == value:
                return False
        for row_all in self.b:
            if row_all[y] == value:
                return False
        row, col = int(x / 3) * 3, int(y / 3) * 3
        row3col3 = self.b[row][col:col + 3] + self.b[row + 1][col:col + 3] + self.b[row + 2][col:col + 3]
        for row3col3_item in row3col3:
            if row3col3_item == value:
                return False
        return True

    def get_next(self, x, y):  # 得到下一个未填项
        for next_soulu in range(y + 1, 9):
            if self.b[x][next_soulu] == 0:
                return x, next_soulu
        for row_n in range(x + 1, 9):
            for col_n in range(0, 9):
                if self.b[row_n][col_n] == 0:
                    return row_n, col_n
        return -1, -1  # 若无下一个未填项，返回-1

    def try_it(self, x, y):  # 主循环
        if self.b[x][y] == 0:
            for i in range(1, 10):  # 从1到9尝试
                self.t += 1
                if self.check(x, y, i):  # 符合 行列宫均无条件 的
                    self.b[x][y] = i  # 将符合条件的填入0格
                    next_x, next_y = self.get_next(x, y)  # 得到下一个0格
                    if next_x == -1:  # 如果无下一个0格
                        return True  # 返回True
                    else:  # 如果有下一个0格，递归判断下一个0格直到填满数独
                        end = self.try_it(next_x, next_y)
                        if not end:  # 在递归过程中存在不符合条件的，即 使try_it函数返回None的项
                            self.b[x][y] = 0  # 回朔到上一层继续
                        else:
                            return True

    def start(self):
        # begin = datetime.datetime.now()
        if self.b[0][0] == 0:
            self.try_it(0, 0)
        else:
            x, y = self.get_next(0, 0)
            self.try_it(x, y)
        s = [i for i in self.b]  # 将计算结果组成一个列表（二维的列表）

        # end = datetime.datetime.now()
        # print('\ncost time:', end - begin)
        # print('times:', self.t)
        return s


if __name__ == '__main__':




    while True:
        app = QApplication(sys.argv)
        MainWindow = myWindow()
        # ui = solutionSudoku.Ui_MainWindow()
        # ui.setupUi(MainWindow)

        MainWindow.show()
        sys.exit(app.exec_())
