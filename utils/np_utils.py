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
# @Program : 数值计算扩展 工具类 | Numerical calculation extension tools
# @File : np_utils.py
# @Description : 定义 数值计算扩展 工具类 | Definition Numerical calculation extension tool class
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 第三方模块 | Import third-party modules
import numpy as np


def prp_2_oh_array(arr):
    """
    定义 矩阵转换 函数 | Definition matrix conversion function
    概率矩阵转换为OH矩阵 | Probability Matrix to OH Matrix
    arr = np.array([[0.1, 0.5, 0.4], [0.2, 0.1, 0.6]])
    :param arr: 概率矩阵 | Probability matrix
    :return: OH矩阵 | OH matrix
    """
    arr_size = arr.shape[1]  # 类别数 | Number of categories
    arr_max = np.argmax(arr, axis=1)  # 最大值位置 | Maximum position
    oh_arr = np.eye(arr_size)[arr_max]  # OH矩阵 | OH matrix
    return oh_arr
