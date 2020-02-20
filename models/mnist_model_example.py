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
# @Program : 自定义 网络结构类 (示例) | Custom network structure class (example)
# @File : mnist_model_example.py
# @Description : 自定义 网络结构类 (示例) | Custom network structure class (example)
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 标准库&内置模块 | Import standard library & built-in modules
import os

# 导入 第三方模块 | Import third-party modules
from keras import Input, Model
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model

# 导入 自定义模块 | Import Custom Module
from bases.model_base import ModelBase


class MnistModelExample(ModelBase):
    """
    定义 自定义 模型示例, 需继承ModelBase基类 | To define a custom model example, you need to inherit the ModelBase base class
    """

    # 覆写 初始化 方法 | Override initialization method
    def __init__(self, config):
        super(MnistModelExample, self).__init__(config)
        self.build_model()

    # 覆写 构建模型 方法 | Override the build model method
    def build_model(self):
        main_input = Input(shape=(28 * 28,), name='main_input')
        x = Dense(
            units=32,
            activation='relu',
            kernel_initializer='random_uniform')(main_input)
        x = Dense(units=16, activation='relu')(x)
        output = Dense(units=10, activation='softmax')(x)
        model = Model([main_input], output)
        model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=self.config.lr),
                      metrics=['accuracy'])

        # 绘制模型图 | Draw a model diagram
        plot_model(
            model,
            to_file=os.path.join(
                self.config.img_dir,
                "resource/demo/model.png"),
            show_shapes=True)

        self.model = model
