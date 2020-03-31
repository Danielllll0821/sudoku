﻿# coding=utf-8
import datetime


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
        begin = datetime.datetime.now()
        if self.b[0][0] == 0:
            self.try_it(0, 0)
        else:
            x, y = self.get_next(0, 0)
            self.try_it(x, y)
        for i in self.b:
            print(i)
        end = datetime.datetime.now()
        print('\ncost time:', end - begin)
        print('times:', self.t)
        return



def GetSudoku():


    sudoku = []
    i = 0

    while i < 9:
        i = i + 1
        row = []  # 重置每行数据为空
        print("请依次输入数组的每" + str(i) + "行，以0代替未知的数字：")
        r = list(input())  # 将输入的每一行数字变成列表，字符串列表
        for R in r:
            row.append(int(R))  # 将字符串列表变成int列表

        sudoku.append(row)  # 把每一行数据的列表加入数独列表

    return sudoku


if __name__ == '__main__':

    s = solution(GetSudoku())
    s.start()