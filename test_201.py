# coding=utf-8

#读取文件中数组
# f = open('d:/Script/sudoku/sudoku.txt')
# line = f.readlines()
#
# newline = []
#
# for l in line:
#     l = l.strip('\n')
#     newline.append(l)
#
# print(newline)

""""""""""""""""""""""""""""""""""""""""""""""""""
# #读取文件中数组
#
# f = open('d:/Script/sudoku/sudoku.txt')
#
# newline =[]
#
# for line in f.readlines():
#     newrow = []
#     line = line.strip('\n')
#     for n in list(line):
#         newrow.append(int(n))
#     newline.append(newrow)
#
#
# print(newline)

''''''''''''''''''''''''''''''''''''''''''''''''''
def GeSudoku(file):
    #读取文件中数组

    f = open(file)

    sudoku =[]

    for line in f.readlines():
        newrow = []
        line = line.strip('\n')
        for n in list(line):
            newrow.append(int(n))
        sudoku.append(newrow)
    # print(sudoku)
    return sudoku



f = 'd:/Script/sudoku/sudoku.txt'
GeSudoku(f)
