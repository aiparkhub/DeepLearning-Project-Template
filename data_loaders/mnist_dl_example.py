# -*- coding:utf-8 -*-
#
# Geek International Park | 极客国际公园 & GeekParkHub | 极客实验室
# Website | https://www.geekparkhub.com
# Description | Open · Creation |
# Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.
#
# HackerParkHub | 黑客公园
# Website | https://www.hackerparkhub.org
# Description | In the spirit of fearless exploration, create unknown technology and worship of technology.
#
# AIParkHub | 人工智能公园
# Website | https://github.com/aiparkhub
# Description | Embark on the wave of AI and push the limits of machine intelligence.
#
# @GeekDeveloper : JEEP-711
# @Author : system
# @Version : 0.2.5
# @Program : 自定义 加载数据类 (示例) | Custom load data class (example)
# @File : mnist_dl_example.py
# @Description : 自定义 加载数据类 (示例) | Custom load data class (example)
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 第三方模块 | Import third-party modules
from keras.datasets import mnist
from keras.utils import to_categorical

# 导入 自定义模块 | Import Custom Module
from bases.data_loader_base import DataLoaderBase


class MnistDLExample(DataLoaderBase):
    '''
    定义 自定义 加载数据类示例, 需继承DataLoaderBase基类 | Define custom load data class example, need to inherit the DataLoaderBase base class
    '''

    # 覆写 初始化 方法 | Override initialization method
    def __init__(self, config=None):
        super(MnistDLExample, self).__init__(config)
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()

        self.X_train = self.X_train.reshape((-1, 28 * 28))
        self.X_test = self.X_test.reshape((-1, 28 * 28))

        self.y_train = to_categorical(self.y_train)
        self.y_test = to_categorical(self.y_test)

        print("[INFO] X_train.shape: %s, y_train.shape: %s"
              % (str(self.X_train.shape), str(self.y_train.shape)))
        print("[INFO] X_test.shape: %s, y_test.shape: %s"
              % (str(self.X_test.shape), str(self.y_test.shape)))

    # 覆写 获取训练数据 方法 | Overwrite Get Training Data Method
    def get_train_data(self):
        return self.X_train, self.y_train

    # 覆写 获取测试数据 方法 | Overwrite test data method
    def get_test_data(self):
        return self.X_test, self.y_test
