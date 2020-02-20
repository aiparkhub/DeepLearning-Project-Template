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
# @Program : 推断基类 | Inferred base class
# @File : infer_base.py
# @Description : 定义 推断基类 | Definition inferred base class
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


class InferBase(object):
    """
    推断基类 | Inferred base class
    """

    # 定义 初始化 方法 | Definition initialization method
    def __init__(self, config):
        # 设置 配置信息 | Setting configuration information
        self.config = config

    # 定义 加载模型 方法 | Definition Load model method
    def load_model(self, name):
        """
        加载模型 | Load the model
        """
        raise NotImplementedError

    # 定义 预测结果 方法 | Definition Forecast result method
    def predict(self, data):
        """
        预测结果 | forecast result
        """
        raise NotImplementedError
