# coding=utf-8


def GetSudoku():


    row = []
    sudoku = []
    i = 0

    while i < 2:
        i = i + 1
        print("请依次输入数组的每" + str(i) + "行，以0代替未知的数字：")

        r = list(input())  # 将输入的每一行数字变成列表，字符串列表
        for R in r:
            row.append(int(R))  # 将字符串列表变成int列表

        sudoku.append(row)  # 把每一行数据的列表加入数独列表
        row = []  # 重置每行数据为空

    return sudoku



s= GetSudoku()
print(s)
