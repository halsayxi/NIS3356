import os

import torch
import torch.nn as nn
from pytorch_pretrained_bert import BertModel, BertTokenizer

# 识别的类型
key = {0: 'legal',
       1: 'illegal',
       }


class Config:
    """配置参数"""

    def __init__(self):
        cru = os.path.dirname(__file__)
        self.class_list = [str(i) for i in range(len(key))]  # 类别名单
        self.save_path = os.path.join(cru, 'ernie/ERNIE.ckpt') #训练好的模型
        self.device = torch.device('cpu')
        self.require_improvement = 1000  # 若超过1000batch效果还没提升，则提前结束训练
        self.num_classes = len(self.class_list)  # 类别数
        self.num_epochs = 3  # epoch数
        self.batch_size = 128  # mini-batch大小
        self.pad_size = 48  # 每句话处理成的长度(短填长切)
        self.learning_rate = 5e-5  # 学习率
        self.bert_path = os.path.join(cru, 'ERNIE_pretrain')    #预训练的ernie
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_path)
        self.hidden_size = 768

    def build_dataset(self, text):
        lin = text.strip()
        pad_size = len(lin)
        token = self.tokenizer.tokenize(lin)
        token = ['[CLS]'] + token
        token_ids = self.tokenizer.convert_tokens_to_ids(token)
        mask=[]
        if len(token) < pad_size:
            mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
            token_ids += ([0] * (pad_size - len(token)))
        else:
            mask = [1] * pad_size
            token_ids = token_ids[:pad_size]
        return torch.tensor([token_ids], dtype=torch.long), torch.tensor([mask])


class Model(nn.Module):

    def __init__(self, config):
        super(Model, self).__init__()
        self.bert = BertModel.from_pretrained(config.bert_path)
        for param in self.bert.parameters():
            param.requires_grad = True
        self.fc = nn.Linear(config.hidden_size, config.num_classes)

    def forward(self, x):
        context = x[0]
        mask = x[1]
        _, pooled = self.bert(context, attention_mask=mask, output_all_encoded_layers=False)
        out = self.fc(pooled)
        return out


config = Config()
model = Model(config).to(config.device)
model.load_state_dict(torch.load(config.save_path, map_location='cpu'))


def prediction_model(text):
    """输入一句问话预测"""
    data = config.build_dataset(text)
    with torch.no_grad():
        outputs = model(data)
        num = torch.argmax(outputs)
    return key[int(num)]


def split_string(string,list): #分成长度不超过48
    if len(string)<=48:
        list.append(string)
        return
    i=48
    while i>0:
          if string[i] in {',','.','。','，','?','？','!','！','@','\'','\"','”','“','’','‘',} :
               break
          i-=1
    if i==0:
         i=48 
    if '\n' not in string[0:i+1]:
        list.append(string[0:i+1]+'\n')
    else:
         list.append(string[0:i+1])  
    split_string(string[i+1:],list)



if __name__ == '__main__':
    input="input/topic_218647_posts.txt"            #输入文件
    output=input.replace('.txt','_result.txt').replace('input','output',1)   #输出文件


    with open(input, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            list=[]
            split_string(line,list)
            for item in list:
                if len(item)>2:
                    data=item.replace('\n','')+'\t'+prediction_model(item)+'\n'
            with open(output, 'ab') as fp2:
                fp2.write(str.encode(data))
