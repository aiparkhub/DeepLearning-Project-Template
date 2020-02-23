# 🎊 DeepLearning-Project-Template 🎊

[![文档更新时间](https://img.shields.io/badge/更新时间-2020%2F02%2F20-darkorchid.svg?style=for-the-badge&logo=codacy&cacheSeconds=3600)]()
[![文档语言-简体中文](https://img.shields.io/badge/文档语言-简体中文-coral.svg?style=for-the-badge&logo=microsoft-word&cacheSeconds=3600)](./README_Simplified_Chinese.md)
[![文档语言-英文](https://img.shields.io/badge/文档语言-英文-mediumpurple.svg?style=for-the-badge&logo=microsoft-word&cacheSeconds=3600)](./README.md)
[![开放源码](https://img.shields.io/badge/开放源码-%E2%9D%A4-brightgreen.svg?style=for-the-badge&logo=conekta&cacheSeconds=3600)]()
[![GitHub Repo Size in Bytes](https://img.shields.io/github/repo-size/aiparkhub/DeepLearning-Project-Template.svg?style=for-the-badge&logo=adobe-creative-cloud&cacheSeconds=3600)]()
[![编程语言-Python](https://img.shields.io/badge/编程语言-Python-blue.svg?style=for-the-badge&logo=python&logoColor=white&cacheSeconds=3600)]()
[![Github组织-AiParkHub](https://img.shields.io/badge/Github组织-aiparkhub-magenta.svg?style=for-the-badge&logo=microsoft-teams&logoColor=white&cacheSeconds=3600)](https://github.com/aiparkhub)
[![网络站点-AiParkHub](https://img.shields.io/badge/网络站点-AIParkHub-yellow.svg?style=for-the-badge&logo=github&cacheSeconds=3600)](https://github.com/aiparkhub)
[![极客开发者-jeep711](https://img.shields.io/badge/极客开发者-jeep711-azure2.svg?style=for-the-badge&logo=opsgenie&cacheSeconds=3600)](https://github.com/jeep711)


<div align="center">
<img src="resource/group_sign/aiparkhub_group_sign.svg" width="450px" alt="AiParkHub-Organization" title="AiParkHub-Organization">
</div><br>

- **AIParkHub-Group | 踏上AI浪潮 推动机器智能的极限**
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>

> [AiParkHub - 深度学习工程模板](https://github.com/aiparkhub/DeepLearning-Project-Template)是基于PEP8(Python Enhancement Proposal #8)之上构建的工程模板, 实现抽象封装公共资源/简化加载数据/构建网络/训练模型/预测样本的工作流程.
>
> [工程地址 : https://github.com/aiparkhub/DeepLearning-Project-Template](https://github.com/aiparkhub/DeepLearning-Project-Template)


## 1. 如何使用
### 1.1 克隆工程
``` bash
git clone https://github.com/aiparkhub/DeepLearning-Project-Template.git
```

### 1.2 创建&激活虚拟环境
``` bash
virtualenv venv
source venv/bin/activate
```

### 1.3 安装Python依赖库
> 1.3.0 ⚠️ 预先检查Python版本 - Python版本应>=3.x.x
``` bash
(base) systemhub:~ system$ python --version
Python 3.7.5
(base) systemhub:~ system$ 
```
> 
> 1.3.1 ⚠️ 预先检查pip版本
``` bash
(base) systemhub:~ system$ pip --version
pip 20.0.2 from /XXX/XXX/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
(base) systemhub:~ system$ pip3 --version
pip 20.0.2 from /XXX/XXX/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
(base) systemhub:~ system$ 
```
> 
> 1.3.2 ⚠️ 如pip版本过低. 应升级更新pip版本 (非低版本跳过此步骤, 进行下一步)
>
> 如pip默认为海外镜像源, 网络连接较差,可临时使国内镜像站升级pip, 升级后再将pip默认设置为国内镜像源.
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```
> 
> 将pip默认设置为国内镜像源
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

>1.3.3 ⚠️ 安装h5py时候可能会出问题, 因为h5py需要编译, 出现的问题一般是gcc或者g++版本的问题, 所以在pip install 之前, 可以通过在命令行键入来临时修改当前终端的环境变量gcc和g++对应位置
```
export CC=/usr/local/bin/gcc
export CXX=/usr/local/bin/g++
```
>
> 1.3.4 基于(中央处理器) CPU版本 | 如有多本版pip, 请使用pip3进行操作
``` bash
pip3 install -r requirements-cpu.txt
```
> 
> 1.3.5 基于(图形处理器) GPU版本 | 如有多本版pip, 请使用pip3进行操作
``` bash
pip3 install -r requirements-gpu.txt
```

### 1.4 自定义 开发流程
> - 1.自定义数据加载类需要继承```DataLoaderBase```;
> - 2.自定义网络结构类需要继承```ModelBase```;
> - 3.自定义模型训练类需要继承```TrainerBase```;
> - 4.自定义样本预测类需要继承```InferBase```;
> - 5.自定义配置文件写入实验的相关参数;
> - 6.执行训练模型和预测样本操作;


## 2. 工程示例
### 2.1 识别 手写数字 示例
> 识别[MNIST](http://yann.lecun.com/exdb/mnist/)库中手写数字, ``simple_mnist``工程示例

#### 2.1.1 训练
``` bash
python main_train.py -c config/simple_mnist_config.json
```

#### 2.1.2 预测
``` bash
python main_test.py -c config/simple_mnist_config.json -m simple_mnist.weights.10-0.24.hdf5
```

#### 2.1.3 网络结构
![网络结构](resource/demo/model.png)
 
#### 2.1.4 TensorBoard
![TensorBoard](resource/demo/tensor_board.png)


## 3. 工程架构
![工程架构](resource/demo/frames.png)

### 3.1 工程树形结构
``` bash
.
├── LICENSE -   Apache2.0 开源许可协议
├── README.md   - (默认英文版)开源文档说明
├── README_Simplified_Chinese.md    -   (简体中文)开源文档说明
├── bases   - 抽象封装 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── data_loader_base.cpython-37.pyc
│   │   ├── infer_base.cpython-37.pyc
│   │   ├── model_base.cpython-37.pyc
│   │   └── trainer_base.cpython-37.pyc
│   ├── data_loader_base.py -   数据加载 基类
│   ├── infer_base.py    -  预测样本(推断) 基类
│   ├── model_base.py   -   网络结构(模型) 基类
│   └── trainer_base.py -   训练模型 基类
├── config              -   配置 文件夹
│   └── simple_mnist_config.json
├── data_loaders    -   自定义 数据加载 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_dl_example.cpython-37.pyc
│   └── mnist_dl_example.py
├── docs    -   文档说明 文件夹
│   └── deep_learning_project_template.rst
├── experiments -   实验数据 文件夹
│   └── simple_mnist    -   实验名称
│       ├── checkpoints -   存储模型&参数检查点
│       ├── images  -   图片存储路径
│       └── logs    -   日志, 如TensorBoard
├── infers  -   自定义 预测类 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_infer_example.cpython-37.pyc
│   └── mnist_infer_example.py
├── main_test.py    -   预测样本 入口
├── main_train.py   -   训练模型 入口
├── models  -   自定义 网络结构 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_model_example.cpython-37.pyc
│   └── mnist_model_example.py
├── requirements-cpu.txt    -   基于CPU-Python依赖库
├── requirements-gpu.txt    -   基于GPU-Python依赖库
├── resource    -   公共资源 文件夹
│   └── demo
│       ├── frames.png
│       ├── model.png
│       └── tensor_board.png
├── root_dir.py -   根目录 工具
├── trainers    -   自定义 训练模型 文件夹
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_trainer_example.cpython-37.pyc
│   └── mnist_trainer_example.py
└── utils   -   工具类 文件夹
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── config_utils.cpython-37.pyc
    │   ├── np_utils.cpython-37.pyc
    │   └── utils.cpython-37.pyc
    ├── config_utils.py -   配置工具类
    ├── np_utils.py -   数值计算扩展工具类
    └── utils.py    -   其他工具类
```

## 4. 工程主要组件
### 4.1 DataLoader
> 自定义 操作步骤：
> - 1.创建自定义的加载数据类,并继承`DataLoaderBase`基类;
> - 2.覆写`get_train_data()`和`get_test_data()`方法, 返回训练和测试数据; 


### 4.2 Model
> 自定义 操作步骤：
> - 1.创建自定义的网络结构类, 并继承`ModelBase`基类;
> - 2.覆写`build_model()`方法, 创建网络结构;
> - 3.在构造器中调用`build_model()`方法;
> - 4.注意: `plot_model()`函数支持绘制网络结构；

### 4.3 Trainer
> 自定义 操作步骤：
> - 1.创建自定义的训练类, 并继承`TrainerBase`基类;
> - 2.参数: 网络结构model、训练数据data;
> - 3.覆写`train()`方法, fit数据, 训练网络结构;
> - 4.注意: 支持在训练中调用callbacks, 额外添加模型存储、TensorBoard、FPR度量等;

### 4.3 Infer
> 自定义 操作步骤：
> - 1.创建自定义的预测类, 并继承`InferBase`基类;
> - 2.覆写`load_model()`方法, 提供模型加载功能;
> - 3.覆写`predict()`方法, 提供样本预测功能;

### 4.5 Config
> 定义在模型训练过程中所需的参数, JSON格式, 支持: 学习率、Epoch、Batch等参数;

### 4.6 Main
#### 4.6.1 训练
> - 1.创建config配置文件;
> - 2.创建dataloader数据加载类实例;
> - 3.创建model网络结构类实例;
> - 4.创建trainer训练类实例, 参数为训练和测试数据、模型;
> - 5.调用执行训练类trainer的`train()`训练函数;

#### 4.6.2 预测
> - 1.创建config配置文件;
> - 2.处理test预测样本;
> - 3.创建infer预测类实例;
> - 4.调用执行预测类infer的`predict()`预测方法;


## 5. 💡如何对该开源文档进行贡献💡

1. Blog内容大多是手敲,所以难免会有笔误,你可以帮我找错别字。
2. 很多知识点我可能没有涉及到,所以你可以对其他知识点进行补充。
3. 现有的知识点难免存在不完善或者错误,所以你可以对已有知识点的修改/补充。
4. 💡欢迎贡献`各领域开源野生Blog`&`笔记`&`文章`&`片段`&`分享`&`创想`&`OpenSource Project`&`Code`&`Code Review`

### 希望每一篇文章都能够对读者们提供帮助与提升,这乃是每一位笔者的初衷                          


-----


## 6.  💌感谢您的阅读 欢迎您的留言与建议💌

- **AIParkHub-Group | 踏上AI浪潮 推动机器智能的极限**
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>


## 7. 捐助 项目的发展离不开你的支持,请开发者喝杯☕Coffee☕吧!
![enter image description here](https://www.geekparkhub.com/docs/images/pay.jpg)


## 8. 感谢 站在巨人肩膀上工作的开发者
参考 [Tensorflow-Project-Template](https://github.com/MrGemy95/Tensorflow-Project-Template)


## 9. License 开源协议
 [Apache License Version 2.0](./LICENSE)
 
 ---------
