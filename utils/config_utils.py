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
# @Program : 配置信息 工具类 | Configuration information
# @File : config_utils.py
# @Description : 定义 配置信息 工具类 | Definition Configuration Information Tool
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 标准库&内置模块 | Import standard library & built-in modules
import argparse
import os
import json

# 导入 第三方模块 | Import third-party modules
from bunch import Bunch

# 导入 自定义模块 | Import Custom Module
from utils.utils import mkdir_if_not_exist


def get_config_from_json(json_file):
    """
    定义 json获取配置信息 函数, 将配置文件转换为配置类 | Define json function to get configuration information, convert configuration file to configuration class
    """
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)  # 配置字典 | Configuration dictionary

    # 将配置字典转换为类 | Converting a configuration dictionary to a class
    config = Bunch(config_dict)

    return config, config_dict


def process_config(json_file):
    """
    定义 解析Json文件 函数 | Definition Parse Json File Function
    :param json_file: 配置文件
    :return: 配置类
    """
    config, _ = get_config_from_json(json_file)
    config.tb_dir = os.path.join("experiments", config.exp_name, "logs/")  # 日志 | Log
    config.cp_dir = os.path.join(
        "experiments",
        config.exp_name,
        "checkpoints/")  # 模型 | model
    config.img_dir = os.path.join(
        "experiments",
        config.exp_name,
        "images/")  # 网络 | internet

    mkdir_if_not_exist(config.tb_dir)  # 创建文件夹 | Create folder
    mkdir_if_not_exist(config.cp_dir)  # 创建文件夹 | Create folder
    mkdir_if_not_exist(config.img_dir)  # 创建文件夹 | Create folder
    return config


def get_train_args():
    """
    定义 添加训练参数 函数 | Definition add training parameter function
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-c', '--cfg',
        dest='config',
        metavar='path',
        default='None',
        help='add a configuration file')
    args = parser.parse_args()
    return args, parser


def get_test_args():
    """
    定义 添加测试路径 函数 | Definition add test path function
    :return: 参数
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-c', '--cfg',
        dest='config',
        metavar='C',
        default='None',
        help='add a configuration file')
    parser.add_argument(
        '-m', '--mod',
        dest='model',
        metavar='',
        default='None',
        help='add a model file')
    args = parser.parse_args()
    return args, parser
