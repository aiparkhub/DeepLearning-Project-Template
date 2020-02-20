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
# @Program : 数据加载基类 | Base class for data loading
# @File : data_loader_base.py
# @Description : 定义 数据加载基类 | Definition Base class for data loading
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


class DataLoaderBase(object):
    """
    数据加载基类 | Data loading base class
    """

    # 定义 初始化 方法 | Definition initialization method
    def __init__(self, config):
        self.config = config  # 设置 配置信息 | Setting configuration information

    # 定义 获取训练数据 方法 | Definition Get training data method
    def get_train_data(self):
        """
        获取训练数据 | Get training data
        """
        raise NotImplementedError

    # 定义 获取测试数据 方法 | Definition Get test data method
    def get_test_data(self):
        """
        获取测试数据 | Get test data
        """
        raise NotImplementedError
