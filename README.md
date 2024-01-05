# 敏感词分析的ERNIE方法
本项目基于https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch

## 使用说明
训练前需要下载好ERNIE_pretrain文件夹中的预训练模型，训练模型输出在task/saved_disc文件夹。

测试时需要将训练好的模型移动至ernie文件夹中，或下载该文件夹中的模型，输入文件在input文件夹中，输出在output文件夹中

```
# 训练：
python run.py

# 测试：
python test.py
```

