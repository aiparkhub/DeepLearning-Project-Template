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
# @Program : 主训练入口 | Main training entrance
# @File : main_train.py
# @Description : 定义 主训练入口 | Definition Main training entrance
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 第三方模块 | Import third-party modules
import numpy as np

# 导入 自定义模块 | Import Custom Module
from data_loaders.mnist_dl_example import MnistDLExample
from infers.mnist_infer_example import MnistInferExample
from models.mnist_model_example import MnistModelExample
from trainers.mnist_trainer_example import MnistTrainerExample
from utils.config_utils import process_config, get_train_args


# 定义 训练 函数 | Definition training model function
def main_train():
    """
    定义 训练模型 函数 | Definition training model function

    参考:
    NumPy FutureWarning
    https://stackoverflow.com/questions/48340392/futurewarning-conversion-of-the-second-argument-of-issubdtype-from-float-to
    """
    print('[INFO] 解析配置...')

    parser = None
    config = None

    # try:
    #     args, parser = get_train_args()
    #     config = process_config(args.config)
    # except Exception as e:
    #     print('[Exception] 配置无效, %s' % e)
    #     if parser:
    #         parser.print_help()
    #     print('[Exception] 参考: python main_train.py -c config/simple_mnist_config.json')
    #     exit(0)
    config = process_config('config/simple_mnist_config.json')

    np.random.seed(47)  # 固定随机数

    print('[INFO] 加载数据...')
    dl = MnistDLExample(config=config)

    print('[INFO] 构造网络...')
    model = MnistModelExample(config=config)

    print('[INFO] 训练网络...')
    trainer = MnistTrainerExample(
        model=model.model,
        data=[dl.get_train_data(), dl.get_test_data()],
        config=config)
    trainer.train()
    print('[INFO] 训练完成...')


def test_main():
    print('[INFO] 解析配置...')
    config = process_config('config/simple_mnist_config.json')

    print('[INFO] 加载数据...')
    dl = MnistDLExample()
    test_data = np.expand_dims(dl.get_test_data()[0][0], axis=0)
    test_label = np.argmax(dl.get_test_data()[1][0])

    print('[INFO] 预测数据...')
    infer = MnistInferExample("simple_mnist.weights.10-0.21.hdf5", config)
    infer_label = np.argmax(infer.predict(test_data))
    print('[INFO] 真实Label: %s, 预测Label: %s' % (test_label, infer_label))

    print('[INFO] 预测完成...')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 调用 test_main 函数 | Call test_main function
    # main_train()
    test_main()
