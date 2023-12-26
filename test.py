# -*- coding:utf-8 -*-

import time
from model import BertTextModel_last_layer
from utils import MyDataset
from transformers import BertTokenizer
from torch.utils.data import DataLoader
import torch
from config import parsers
from colorama import Fore, Style

def load_model(model_path, device):
    model = BertTextModel_last_layer().to(device)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def text_class_name(index, text, pred, args, output_file):
    results = torch.argmax(pred, dim=1)
    results = results.cpu().numpy().tolist()
    classification = open(args.classification, "r", encoding="utf-8").read().split("\n")
    classification_dict = dict(zip(range(len(classification)), classification))
    
    with open(output_file, 'a', encoding='utf-8') as file:
        if len(results) != 1:
            for i in range(len(results)):
                file.write(f"索引：{index[i]}\t文本：{text[i]}\t预测的类别为：{classification_dict[results[i]]}\n")
        else:
            file.write(f"索引：{index[0]}\t文本：{text}\t预测的类别为：{classification_dict[results[0]]}\n")

def pred_from_txt(args, model, device, start, output_file):
    txt_path = 'input/topic_217915_posts.txt'  # 替换为你的 txt 文件路径
    with open(txt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    indices = [line.strip().split('\t')[0] for line in lines]
    texts = [line.strip().split('\t')[1] for line in lines]

    x = MyDataset(texts, labels=None, with_labels=False)
    xDataloader = DataLoader(x, batch_size=len(texts), shuffle=False)

    for batch_index, batch_con in enumerate(xDataloader):
        batch_con = tuple(p.to(device) for p in batch_con)
        pred = model(batch_con)
        text_class_name(indices, texts, pred, args, output_file)

    end = time.time()
    print(f"耗时为：{end - start} s")

if __name__ == "__main__":
    start = time.time()
    args = parsers()
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    model = load_model(args.save_model_best, device)

    output_file = 'output/output_217915.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("索引\t文本\t模型预测结果\n")

    pred_from_txt(args, model, device, start, output_file)

    print(f"预测结果已写入 {output_file}")
