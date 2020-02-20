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
# @Program : 自定义 加载数据类 | Custom load data class
# @File : mnist_dl_examples.py
# @Description : 自定义 加载数据类 | Custom load data class
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.

# 导入第三方模块 | Import third-party modules
from keras.datasets import mnist
from keras.utils import to_categorical
from bases.data_loader_base import DataLoaderBase


class SimpleMnistDL(DataLoaderBase):
    '''
    自定义 加载数据类, 需继承DataLoaderBase基类 |Custom load data class, need to inherit the DataLoaderBase base class
    '''

    # 定义 初始化 方法 | Definition initialization method
    def __init__(self, config=None):
        super(SimpleMnistDL, self).__init__(config)
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()

        self.X_train = self.X_train.reshape((-1, 28 * 28))
        self.X_test = self.X_test.reshape((-1, 28 * 28))

        self.y_train = to_categorical(self.y_train)
        self.y_test = to_categorical(self.y_test)

        print("[INFO] X_train.shape: %s, y_train.shape: %s"
              % (str(self.X_train.shape), str(self.y_train.shape)))
        print("[INFO] X_test.shape: %s, y_test.shape: %s"
              % (str(self.X_test.shape), str(self.y_test.shape)))

    # 复写 获取训练数据 方法 | Replication Get Training Data Method
    def get_train_data(self):
        return self.X_train, self.y_train

    # 复写 获取测试数据 方法 | Retrieve test data method
    def get_test_data(self):
        return self.X_test, self.y_test
