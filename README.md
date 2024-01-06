# 水源社区智能提取与言论审查系统



## 项目目录：

```
NIS3356   
    |-- bert-base-chinese    存放bert中文预训练模型  
    |-- crawler              存放信息收集代码，包含信息收集需要的安装包requirement.txt
    |-- data                 存放数据集   
    |-- model                存放训练好的bert模型  
    |-- Sound_Shape_Code     存放敏感词检测的音形码模型
    |-- config.py            bert-配置文件   
    |-- main.py              bert-模型训练主函数
    |-- model.py             bert-模型文件 
    |-- predict.py		     bert-模型预测
    |-- summary.py           帖子摘要总结代码
    |-- test_ac.py           图形化交互文件1
    |-- test.py              图形化交互文件2
    |-- requirement.txt      bert-需要的安装包
    |-- result.txt           bert-训练一轮的结果
    |-- utils.py             bert-数据处理文件
    
```



## 分支介绍：

1. main 分支：代码仓库的主要分支，包含整个项目的最终版本，包括信息收集、摘要总结、敏感词分析以及图形化界面的所有功能。
2. crawler 分支：信息收集的分支
3. Text_Classification_bert 分支：关于敏感词分析中基于 BERT-base-chinese+TextCNN 架构的二分类方法的源代码，包括预训练模型、训练好的模型、训练和测试代码等，仅支持命令行交互。
4. Text_Classification_erine 分支：同上，是敏感词分析中基于 ERNIE+Linear 架构的二分类方法的源代码。
5. Sound_Shape_Code 分支：关于敏感词分析中音形码的源代码，包括敏感词库和测试代码，仅支持命令行交互。




## 测试方法
1. 在model文件夹下载训练好的模型：https://jbox.sjtu.edu.cn/l/G1Mt5V
2. 在bert-base-chinese文件夹下载bert中文预训练模型：https://huggingface.co/bert-base-chinese/tree/main
2. 在crawler/cookies.txt中添加自己的水源社区cookies
3. 运行基于Bert的敏感词分析与帖子摘要：`python test.py`
4. 运行基于音节的敏感词分析：`python test_ac.py`
