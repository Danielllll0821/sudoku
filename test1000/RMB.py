import numpy as np
from matplotlib import pyplot as plt

'''
# 国际黄金的报价是以美元计价的。
# 重量是以盎司为单位。
# 国内黄金是以人民币计价，重量以克为单位。
# 比如国际黄金现价1250美元/盎司，国内黄金270元/克
# 
# 1盎司=31.1035克
# 
# 1250/31.1035*当天汇率=270
x =270 
y = 270/7 *31.1035
'''

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x = np.arange(0, 500)
y = x / 7 * 31.1035


def zuobiao(x):
    y = x / 7 * 31
    return y


plt.axis([0, 700, 0, 3000])  # 坐标轴的范围
plt.title("黄金换算")
plt.xlabel("人民币(克)", fontproperties="SimSun")  # X轴的名字，字体为黑体
plt.ylabel("美元(盎司)", fontproperties="SimSun")

# plt.scatter(300, zuobiao(300), s=20, color='b')  # 指定坐标点
# plt.plot([300, 300], [0, zuobiao(300)], 'k:', lw=2.5)  # 画一条线，起点是x轴的300，终点是对应y值
# plt.plot([0, 300], [zuobiao(300), zuobiao(300)], 'k:', lw=2.5)
# plt.annotate((r'$ (%d) $' % zuobiao(300)), xy=(300, 300 / 7 * 31.1035 - 100))  # 注释。(注释内容，注释所在坐标）


def showValue(x):
    # 根据X值画出对应的坐标点(x,y),并分别画出坐标点到x轴和y轴的虚线。

    plt.scatter(x, zuobiao(x), s=20, color='b')  # 指定坐标点
    plt.plot([x, x], [0, zuobiao(x)], 'k:', lw=2.5)  # 画一条线，起点是x轴的300，终点是对应y值
    plt.plot([0, x], [zuobiao(x), zuobiao(x)], 'k:', lw=2.5)
    plt.annotate((r'$ (%d) $' % zuobiao(x)), xy=(0, x / 7 * 31.1035 - 100))  # 注释。(注释内容，注释所在坐标）
    plt.annotate((r'$ (%d) $' % x), xy=(x, 50))  # 注释。(注释内容，注释所在坐标）


showValue(390)

plt.plot(x, y)
plt.show()
