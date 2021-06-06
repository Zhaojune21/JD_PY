# 注意

本项目是基于python3.9写的，不保证低版本python兼容性

不依赖于任何容器，可以单独运行。你可以选择使用docker运行，也可以选择直接宿主机运行。推荐docker运行，虽然我没做过docker的测试，但由于项目涉及到crontab的编辑，因此宿主机运行可能会导致crontab清空，所以docker更安全

# 使用方法
## 一、下载本项目
`git clone https://github.com/dd178/JD_PY.git`

## 二、初始化
```
cd JD_PY
cp config/JD_PY_BOT.conf.example config/JD_PY_BOT.conf
mkdir logs
```

## 三、修改配置文件

修改config文件夹中的JD_PY_BOT.conf

## 四、安装依赖

```pip install -r requirements.txt```

## 五、运行程序

### 1.前台运行（不推荐）
```python JD_PY.py```

### 2.nohup命令（推荐）
```nohup python JD_PY.py &```

### 3.screen命令（推荐）
#### 3.1 ubuntu安装
```apt install screen```
#### 3.2 CentOS安装
```yum install screen```
其他系统请自行百度
#### 3.3 基本命令
```screen -S name``` 新建一个名称为name的会话

```screen -r name``` 回到name会话

```screen -X -S name quit``` 结束name会话

```screen -ls``` 查看所有会话

```ctrl+a+d``` 使用组合键返回主会话

#### 3.4 使用
```screen -S JD_PY```新建JD_PY会话

```python JD_PY.py```运行程序

```ctrl+a+d```返回
