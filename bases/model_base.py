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
# @Program : 模型基类 | Model base class
# @File : model_base.py
# @Description : 定义 模型基类 | Definition model base class
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


class ModelBase(object):
    """
    模型基类 | Model base class
    """

    # 定义 初始化 方法 | Definition initialization method
    def __init__(self, config):
        self.config = config  # 设置 配置信息 | Setting configuration information
        self.model = None  # 设置 模型 | Setting up the model

    # 定义 保存模型 方法 | Definition save model method
    def save(self, checkpoint_path):
        """
        Define storage checkpoints, paths are defined in configuration files
        定义 存储检查点, 路径定义于配置文件中
        """
        if self.model is None:
            raise Exception("[Exception] You have to build the model first.")

        print("[INFO] Saving Model...")
        self.model.save_weights(checkpoint_path)
        print("[INFO] Model Saved")

    # 定义 加载模型 方法 | Definition load model method
    def load(self, checkpoint_path):
        """
        Load storage checkpoint, path is defined in configuration file
        加载存储检查点, 路径定义于配置文件中
        """
        if self.model is None:
            raise Exception("[Exception] You have to build the model first.")

        print("[INFO] Loading model checkpoint {} ...\n".format(checkpoint_path))
        self.model.load_weights(checkpoint_path)
        print("[INFO] Model Loaded")

    # 定义 构建模型 方法 | Definition build model method
    def build_model(self):
        """
        构建模型 | Building the model
        """
        raise NotImplementedError
