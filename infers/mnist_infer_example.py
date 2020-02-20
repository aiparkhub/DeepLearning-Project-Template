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
# @Program : 自定义 预测类 (示例) | Custom Forecasting Class (example)
# @File : mnist_infer_example.py
# @Description : 自定义 预测类 (示例) | Custom Forecasting Class (example)
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 标准库&内置模块 | Import standard library & built-in modules
import os

# 导入 第三方模块 | Import third-party modules
from keras.models import load_model

# 导入 自定义模块 | Import Custom Module
from bases.infer_base import InferBase


class MnistInferExample(InferBase):
    '''
    定义 自定义 预测类示例, 需继承InferBase基类 | Define a custom prediction class example, which needs to inherit the InferBase base class
    '''

    # 覆写 初始化 方法 | Override initialization method
    def __init__(self, name, config=None):
        super(MnistInferExample, self).__init__(config)
        self.model = self.load_model(name)

    # 覆写 加载模型 方法 | Overwrite load model method
    def load_model(self, name):
        model = os.path.join(self.config.cp_dir, name)
        return load_model(model)

    # 覆写 预测 方法 | Overwrite prediction method
    def predict(self, data):
        return self.model.predict(data)
