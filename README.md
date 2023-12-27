模型都未进行调参，未能使模型的准确率达到最高

# 项目名称：

使用 Bert + TextCNN 融合模型来对中文进行分类，即文本分类
Bert往往可以对一些表述隐晦的句子进行更好的分类，TextCNN往往对关键词更加敏感。

# 项目环境：

pytorch、python   
相关库安装
`pip install -r requirement.txt`

# 项目目录：

```
NIS3356  
    |-- bert-base-chinese    bert 中文预训练模型     
    |-- data                 数据集              
    |-- model                保存的模型               
    |-- config.py            配置文件                   
    |-- log.py               日志文件                 
    |-- main.py              主函数                      
    |-- model.py             模型文件                     
    |-- predict.py           预测文件                         
    |-- requirement.txt      需要的安装包
    |-- result.txt           训练一轮的结果
    |-- utils.py             数据处理文件
    |-- Sound_Shape_Code     音节分析模型
    |-- crawler              爬取网页内容
```


# 模型训练

`python main.py`

# 模型预测

`python predict.py`

# 训练自己的数据集

train.txt、dev.txt、test.txt 的数据格式：文本\t标签（数字表示）

class.txt：标签类别（文本）

## 修改内容：

在配置文件中修改长度、类别数、预训练模型地址    

```
parser.add_argument("--select_model_last", type=bool, default=True, help="选择模型")
parser.add_argument("--bert_pred", type=str, default="./bert-base-chinese", help="bert 预训练模型")
parser.add_argument("--class_num", type=int, default=10)   
parser.add_argument("--max_len", type=int, default=38)
```



# NIS3356

1. 在bert-base-chinese文件夹下载bert 中文预训练模型（见/bert-base-chinese/README）
2. 在model文件夹存放训练好的模型，请先下载：https://pan.quark.cn/s/a53540f93bd1
3. 运行基于Bert的敏感词分析与摘要`python test.py`
4. 运行基于音节的敏感词分析`python test_ac.py`
