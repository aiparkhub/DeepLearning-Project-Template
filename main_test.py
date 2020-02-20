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
# @Program : 主测试入口 | Main test entrance
# @File : main_test.py
# @Description : 定义 主测试入口 | Definition Main test entry
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 第三方模块 | Import third-party modules
import numpy as np

# 导入 自定义模块 | Import Custom Module
from data_loaders.mnist_dl_example import MnistDLExample
from infers.mnist_infer_example import MnistInferExample
from utils.config_utils import process_config, get_test_args


# 定义 测试 函数 | Define test function


def main_test():
    '''
    定义 测试 函数 | Define test function
    '''

    print('[INFO] 解析配置...')
    parser = None
    config = None
    model_path = None

    try:
        args, parser = get_test_args()
        config = process_config(args.config)
        model_path = args.model
    except Exception as e:
        print('[Exception] 配置无效, %s' % e)
        if parser:
            parser.print_help()
        print(
            '[Exception] 参考: python main_test.py -c config/simple_mnist_config.json '
            '-m simple_mnist.weights.10-0.24.hdf5')
        exit(0)
    # config = process_config('config/simple_mnist_config.json')

    np.random.seed(47)  # 固定随机数

    print('[INFO] 加载数据...')
    dl = MnistDLExample()
    test_data = np.expand_dims(dl.get_test_data()[0][0], axis=0)
    test_label = np.argmax(dl.get_test_data()[1][0])

    print('[INFO] 预测数据...')
    # infer = MnistInferExample("simple_mnist.weights.16-0.19.hdf5", config)
    infer = MnistInferExample(model_path, config)
    infer_label = np.argmax(infer.predict(test_data))
    print('[INFO] 真实Label: %s, 预测Label: %s' % (test_label, infer_label))

    print('[INFO] 预测完成...')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用 main_test 函数 | Call main_test function
    main_test()
