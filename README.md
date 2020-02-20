# 🎊 DeepLearning-Project-Template 🎊

@(Update time:2020-02-20) [Document Language : [Simplified Chinese](./README_Simplified_Chinese.md) & [English](./README.md) | Programming Language : Python | Website : [AIParkHub](https://github.com/aiparkhub) | GeekDeveloper : [JEEP-711](https://github.com/jeep711) | Github : [github.com/aiparkhub](https://github.com/aiparkhub) | ![OpenSource](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg) | ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/aiparkhub/DeepLearning-Project-Template.svg) ]

<div align="center">
<img src="resource/group_sign/aiparkhub_group_sign.svg" width="450px" alt="AIParkHub-Group">
</div><br>

- **AIParkHub-Group | Embarking on the AI ​​wave, pushing the limits of machine intelligence**
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>

> [AiParkHub - DeepLearning-Project-Template](https://github.com/aiparkhub/DeepLearning-Project-Template)It is an engineering template built on top of PEP8 (Python Enhancement Proposal # 8), which implements the workflow of abstractly encapsulating common resources / simplifying loading data / building networks / training models / predicting samples.
>
> [Project Address : https://github.com/aiparkhub/DeepLearning-Project-Template](https://github.com/aiparkhub/DeepLearning-Project-Template)


## 1. how to use
### 1.1 Clone engineering
``` bash
git clone https://github.com/aiparkhub/DeepLearning-Project-Template.git
```

### 1.2 Create & Activate Virtual Environment
``` bash
virtualenv venv
source venv/bin/activate
```

### 1.3 Install Python dependencies
> 1.3.0 ⚠️ Check Python version in advance-Python version should be> = 3.x.x
``` bash
(base) systemhub:~ system$ python --version
Python 3.7.5
(base) systemhub:~ system$ 
```
> 
> 1.3.1 ⚠️ Check pip version in advance
``` bash
(base) systemhub:~ system$ pip --version
pip 20.0.2 from /XXX/XXX/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
(base) systemhub:~ system$ pip3 --version
pip 20.0.2 from /XXX/XXX/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
(base) systemhub:~ system$ 
```
> 
> 1.3.2 ⚠️ If pip version is too low. Pip version should be upgraded (non-low version skip this step, proceed to the next step)
>
> If pip is the overseas mirror source by default and the network connection is poor, you can temporarily make the domestic mirror station upgrade pip, and then set pip as the domestic mirror source by default after the upgrade.
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```
> 
> Set pip as the domestic mirror source by default
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

>1.3.3 ⚠️ There may be problems when installing h5py. Because h5py needs to be compiled, the problem usually occurs with the gcc or g ++ version. Before pip install, you can temporarily modify the corresponding environment variable gcc and g ++ by typing on the command line.
```
export CC=/usr/local/bin/gcc
export CXX=/usr/local/bin/g++
```
>
> 1.3.4 Based on (Central Processing Unit) CPU version | If there are multiple versions of pip, please use pip3 for operation
``` bash
pip3 install -r requirements-cpu.txt
```
> 
> 1.3.5 Based on (graphics processor) GPU version | If there are multiple versions of pip, please use pip3 for operation
``` bash
pip3 install -r requirements-gpu.txt
```

### 1.4 Custom development process
> - 1.Custom data loading classes need to inherit ```DataLoaderBase```;
> - 2.Custom network structure classes need to inherit ```ModelBase```;
> - 3.Custom model training classes need to inherit ```TrainerBase```;
> - 4.Custom sample prediction classes need to inherit ```InferBase```;
> - 5.Related parameters for custom configuration file writing experiment;
> - 6.Perform training model and prediction sample operations;


## 2. Engineering Example
### 2.1 Recognition handwritten digits example
> Identify[MNIST](http://yann.lecun.com/exdb/mnist/)Handwritten numbers in library, ``simple_mnist``Engineering example

#### 2.1.1 Training
``` bash
python main_train.py -c config/simple_mnist_config.json
```

#### 2.1.2 Prediction
``` bash
python main_test.py -c config/simple_mnist_config.json -m simple_mnist.weights.10-0.24.hdf5
```

#### 2.1.3 Network structure
![Network structure](resource/demo/model.png)
 
#### 2.1.4 TensorBoard
![TensorBoard](resource/demo/tensor_board.png)


## 3. Engineering architecture
![Engineering architecture](resource/demo/frames.png)

### 3.1 Engineering Tree Structure
``` tree
.
├── LICENSE -   Apache2.0 Apache2.0 open source license agreement
├── README.md   - (Default English version) open source documentation
├── README_Simplified_Chinese.md    -   (Simplified Chinese) Open Source Documentation
├── bases   - Abstract package folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── data_loader_base.cpython-37.pyc
│   │   ├── infer_base.cpython-37.pyc
│   │   ├── model_base.cpython-37.pyc
│   │   └── trainer_base.cpython-37.pyc
│   ├── data_loader_base.py -   Data loading base class
│   ├── infer_base.py    -  Prediction Sample (Inferred) Base Class
│   ├── model_base.py   -   Network Structure (Model) Base Class
│   └── trainer_base.py -   Training Model Base Class
├── config              -   Configuration folder
│   └── simple_mnist_config.json
├── data_loaders    -   Custom data load folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_dl_example.cpython-37.pyc
│   └── mnist_dl_example.py
├── docs    -   Document description
│   └── deep_learning_project_template.rst
├── experiments -   Experiment data folder
│   └── simple_mnist    -   Experiment name
│       ├── checkpoints -   Storage model & parameter checkpoint
│       ├── images  -   Picture storage path
│       └── logs    -   Logs, such as TensorBoard
├── infers  -   Custom Forecasting Folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_infer_example.cpython-37.pyc
│   └── mnist_infer_example.py
├── main_test.py    -   Prediction sample
├── main_train.py   -   Training model entrance
├── models  -   Custom network structure folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_model_example.cpython-37.pyc
│   └── mnist_model_example.py
├── requirements-cpu.txt    -   CPU-Python based libraries
├── requirements-gpu.txt    -   GPU-Python based library
├── resource    -   Public resources folder
│   └── demo
│       ├── frames.png
│       ├── model.png
│       └── tensor_board.png
├── root_dir.py -   Root directory tool
├── trainers    -   Custom training model folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── mnist_trainer_example.cpython-37.pyc
│   └── mnist_trainer_example.py
└── utils   -   Tools folder
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── config_utils.cpython-37.pyc
    │   ├── np_utils.cpython-37.pyc
    │   └── utils.cpython-37.pyc
    ├── config_utils.py -   Configuration tool class
    ├── np_utils.py -   Numerical calculation extension tools
    └── utils.py    -   Other tools
```

## 4. Engineering Main Components
### 4.1 DataLoader
> Custom operation steps：
> - 1.Create a custom load data class and inherit the `Data Loader Base` base class;
> - 2.Override `get_train_data()` and `get_test_data()` methods, return training and test data; 


### 4.2 Model
> Custom operation steps：
> - 1.Create a custom network structure class, and inherit the `ModelBase` base class
> - 2.Override the `build_model()` method to create a network structure;
> - 3.Call the `build model()` method in the constructor;
> - 4.Note: `plot_model()` function supports drawing network structure;

### 4.3 Trainer
> Custom operation steps：
> - 1.Create a custom training class and inherit the `TrainerBase` base class;
> - 2.Parameters: network structure model, training data data;
> - 3.Override `train()` method, fit data, train network structure;
> - 4.Note: Callbacks are supported during training, and additional model storage, TensorBoard, FPR metrics, etc. are added;

### 4.3 Infer
> Custom operation steps：
> - 1.Create a custom forecasting class and inherit the `InferBase` base class;
> - 2.Override the `load_model()` method to provide model loading functionality;
> - 3.Override the `predict()` method to provide sample prediction capabilities;

### 4.5 Config
> Define the parameters required in the model training process, JSON format, support: learning rate, Epoch, Batch and other parameters;

### 4.6 Main
#### 4.6.1 Training
> - 1.Create config configuration file;
> - 2.Create a dataloader data loading class instance;
> - 3.Create a model network structure class instance;
> - 4.Create a trainer training class instance with parameters for training and test data and models;
> - 5.Call the `train()` training function that executes the training class trainer;

#### 4.6.2 Prediction
> - 1.Create config configuration file;
> - 2.Processing test prediction samples;
> - 3.Create an infer prediction class instance;
> - 4.Invoke the `predict()` method of executing the prediction class infer;


## 5.💡How to contribute to this open source document💡

1. Blog content is mostly typed by hand, so there will inevitably be typos. You can help me find the typo.
2. I may not have covered a lot of knowledge points, so you can supplement other knowledge points.
3. Existing knowledge points are inevitably imperfect or wrong, so you can modify / add to existing knowledge points.
4. 💡Welcome to contribute `Open source wild blogs in various fields` &` notes` & `articles && fragments` &` share` & `creation` &` OpenSource Project` & `Code` &` Code Review`

### I hope that each article can help and improve readers, this is the original intention of each author                         


-----


## 6. 💌Thank you for reading, welcome your message and suggestion💌

- **AIParkHub-Group | Embarking on the AI ​​wave, pushing the limits of machine intelligence**
- **`Official Public Email`**
- Group Email：<geekparkhub@outlook.com> —— <hackerparkhub@outlook.com> —— <hackerpark@hotmail.com>
- User Email：<jeep711.home.@gmail.com> —— <jeep-711@outlook.com>
- System Email：<systemhub-711@outlook.com>
- Service Email：<servicehub-711@outlook.com>


## 7.The development of the donation project cannot be separated from your support. Please ask the developer for a cup of coffee!
![enter image description here](https://www.geekparkhub.com/docs/images/pay.jpg)


## 8.Thanks to developers working on giant shoulders
> Reference[Tensorflow-Project-Template](https://github.com/MrGemy95/Tensorflow-Project-Template)


>## 9.License open source agreement
 [Apache License Version 2.0](./LICENSE)
 
 ---------
