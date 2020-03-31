# coding:utf-8

# 导入必要的模块
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
import sys


class My_Main_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(My_Main_window, self).__init__(parent)
        # 重新调整大小
        self.resize(800, 659)
        # 添加菜单中的按钮
        self.menu = QtWidgets.QMenu("绘图")
        self.menu_action = QtWidgets.QAction("绘制", self.menu)
        self.menu.addAction(self.menu_action)
        self.menuBar().addMenu(self.menu)
        # 添加事件
        self.menu_action.triggered.connect(self.plot_)
        self.setCentralWidget(QtWidgets.QWidget())

    # 绘图方法
    def plot_(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        fig = plt.figure()  # 新建一绘图figure
        # 在绘图中新建区域，figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
        # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.set_xlim([0, 600])  # 设置X轴刻度
        ax.set_ylim([0, 2000])  # 设置X轴刻度

        x = np.arange(0, 500)
        y = x / 7 * 31.1035

        ax.plot(x, y)  # 画图
        cavans = FigureCanvas(fig)
        # 将绘制好的图像设置为中心 Widget
        self.setCentralWidget(cavans)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()
