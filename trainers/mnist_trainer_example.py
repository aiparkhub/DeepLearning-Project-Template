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
# @Program : 自定义 训练类 (示例) | Custom training class (example)
# @File : mnist_trainer_example.py
# @Description : 自定义 训练类 (示例) | Custom training class (example)
# @Copyright © 2019 - 2020 AIParkHub-Group. All rights reserved.


# 导入 标准库&内置模块 | Import standard library & built-in modules
import os
import warnings

# 导入 第三方模块 | Import third-party modules
from keras.callbacks import TensorBoard, ModelCheckpoint, Callback
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.metrics import precision_recall_fscore_support
import numpy as np

# 导入 自定义模块 | Import Custom Module
from bases.trainer_base import TrainerBase
from utils.np_utils import prp_2_oh_array


class MnistTrainerExample(TrainerBase):
    '''
    定义 自定义 训练示例, 需继承TrainerBase基类 | Define a custom training example, which needs to inherit the TrainerBase base class
    '''

    # 覆写 初始化 方法 | Override initialization method
    def __init__(self, model, data, config):
        super(MnistTrainerExample, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []
        self.init_callbacks()

    # 定义 初始化回调 方法 | Define the initialization callback method
    def init_callbacks(self):
        self.callbacks.append(
            ModelCheckpoint(
                filepath=os.path.join(
                    self.config.cp_dir,
                    '%s.weights.{epoch:02d}-{val_loss:.2f}.hdf5' %
                    self.config.exp_name),
                monitor="val_loss",
                mode='min',
                save_best_only=True,
                save_weights_only=False,
            ))

        self.callbacks.append(
            TensorBoard(
                log_dir=self.config.tb_dir,
                write_images=True,
                write_graph=True,
            )
        )

        # self.callbacks.append(FPRMetric())
        self.callbacks.append(FPRMetricDetail())

    # 覆写 训练 方法 | Overwrite training method
    def train(self):
        history = self.model.fit(
            self.data[0][0], self.data[0][1],
            epochs=self.config.num_epochs,
            verbose=2,
            batch_size=self.config.batch_size,
            validation_data=(self.data[1][0], self.data[1][1]),
            # validation_split=0.25,
            callbacks=self.callbacks,
        )
        self.loss.extend(history.history['loss'])
        self.acc.extend(history.history['acc'])
        self.val_loss.extend(history.history['val_loss'])
        self.val_acc.extend(history.history['val_acc'])


class FPRMetric(Callback):
    """
    定义 FPR指标类, 输出F, P, R | Define FPR indicator class, output F, P, R
    """

    # 定义 指标 方法 | Definition index method
    def on_epoch_end(self, batch, logs=None):
        val_x = self.validation_data[0]
        val_y = self.validation_data[1]

        prd_y = prp_2_oh_array(np.asarray(self.model.predict(val_x)))

        warnings.filterwarnings("ignore", category=UndefinedMetricWarning)
        precision, recall, f_score, _ = precision_recall_fscore_support(
            val_y, prd_y, average='macro')
        print(
            " — val_f1: % 0.4f — val_pre: % 0.4f — val_rec % 0.4f" %
            (f_score, precision, recall))


class FPRMetricDetail(Callback):
    """
    定义 FPR指标详细信息类, 输出F, P, R | Define FPR indicator details class, output F, P, R
    """

    # 定义 指标 方法 | Definition index method
    def on_epoch_end(self, batch, logs=None):
        val_x = self.validation_data[0]
        val_y = self.validation_data[1]

        prd_y = prp_2_oh_array(np.asarray(self.model.predict(val_x)))

        warnings.filterwarnings("ignore", category=UndefinedMetricWarning)
        precision, recall, f_score, support = precision_recall_fscore_support(
            val_y, prd_y)

        for p, r, f, s in zip(precision, recall, f_score, support):
            print(
                " — val_f1: % 0.4f — val_pre: % 0.4f — val_rec % 0.4f - ins %s" %
                (f, p, r, s))
