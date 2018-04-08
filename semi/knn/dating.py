"""
假设有一个带有标签的样本数据集（训练样本集），其中包含每条数据与所属分类的对应关系。
输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较。
计算新数据与样本数据集中每条数据的距离。
对求得的所有距离进行排序（从小到大，越小表示越相似）。
取前 k （k 一般小于等于 20 ）个样本数据对应的分类标签。
求 k 个数据中出现次数最多的分类标签作为新数据的分类。

收集数据：提供文本文件
准备数据：使用 Python 解析文本文件
分析数据：使用 Matplotlib 画二维散点图
训练算法：此步骤不适用于 k-近邻算法
测试算法：使用海伦提供的部分数据作为测试样本。
        测试样本和非测试样本的区别在于：
            测试样本是已经完成分类的数据，如果预测分类与实际类别不同，则标记为一个错误。
使用算法：产生简单的命令行程序，然后海伦可以输入一些特征数据以判断对方是否为自己喜欢的类型。
"""

import matplotlib.pyplot as plt
import numpy as np


def file2matrix():
    """
    每年获得的飞行常客里程数
    玩视频游戏所耗时间百分比
    每周消费的冰淇淋公升数
    """
    with open('dating.txt') as f:
        lines = f.readlines()
        mat = np.ma.zeros((len(lines), 3))
        vector = []
        for index, l in enumerate(lines):
            l = l.strip().split('\t')
            mat[index] = l[0:3]
            vector.append(int(l[-1]))
    return mat, vector


def draw():
    fig = plt.figure()
    # 绘制 1×1网格，第一子图
    ax = fig.add_subplot(111)
    mat, vector = file2matrix()
    ax.scatter(
        mat[:,0],
        mat[:,1],
        15.0 * np.ma.array(vector),
        np.ma.array(vector),
    )
    plt.show()


if __name__ == '__main__':
    draw()
