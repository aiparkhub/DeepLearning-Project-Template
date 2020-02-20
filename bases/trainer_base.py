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
# @Program : 训练器基类 | Trainer base class
# @File : trainer_base.py
# @Description : 定义 训练器基类 | Define the base class of the trainer
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


class TrainerBase(object):
    """
    训练器基类 | Trainer base class
    """

    # 定义 初始化 方法 | Definition initialization method
    def __init__(self, model, data, config):
        self.model = model  # 设置 模型 | Setting up the model
        self.data = data  # 设置 数据 | Setting data
        self.config = config  # 设置 配置信息 | Setting configuration information

    # 定义 训练 方法 | Define training method
    def train(self):
        """
        训练逻辑 | Training logic
        """
        raise NotImplementedError
