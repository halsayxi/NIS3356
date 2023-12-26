import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
import time
from model import BertTextModel_last_layer
from utils import MyDataset
from transformers import BertTokenizer
from torch.utils.data import DataLoader
import torch
from config import parsers
from colorama import Fore, Style
import summary  # 导入summary.py文件


def run_main(tree, run_button, back_button, text_widget):
    # 你的main函数
    def main():
        start = time.time()
        args = parsers()
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        model = load_model(args.save_model_best, device)

        output_file = 'output.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("模型预测结果：\n")

        pred_from_txt(args, model, device, start, output_file, tree)

        print(f"预测结果已写入 {output_file}")

        # 调用summary.py的main函数，并将结果显示在GUI中
        result = summary.main()
        text_widget.insert(tk.END, result)
        text_widget.see(tk.END)  # 自动滚动到最后一行

    # 使用一个新的线程来运行main函数，以防止它阻塞GUI
    threading.Thread(target=main).start()

    # 隐藏运行按钮，显示返回按钮
    run_button.pack_forget()
    back_button.pack()


def create_gui():
    window = tk.Tk()
    window.title("我的GUI")
    window.geometry('800x650')  # 设置窗口大小

    # 创建一个标签，标记列表部分
    label1 = tk.Label(window, text="评论列表：")
    label1.pack()

    # 创建一个表格
    tree = ttk.Treeview(window, columns=('评论内容', '判决结果'), show='headings', height=15)  # 设置高度为20行
    tree.column('评论内容', width=600, anchor='center')  # 调整列的宽度
    tree.column('判决结果', width=200, anchor='center')  # 调整列的宽度
    tree.heading('评论内容', text='评论内容')
    tree.heading('判决结果', text='判决结果')
    tree.pack()

    # 创建一个分界线
    separator = ttk.Separator(window, orient='horizontal')
    separator.pack(fill='x')

    # 创建一个标签，标记总结文本框部分
    label2 = tk.Label(window, text="总结：")
    label2.pack()

    # 创建一个滚动文本框，用于显示summary.py的结果
    text_widget = scrolledtext.ScrolledText(window, width=100, height=18)
    text_widget.pack()

    # 创建一个运行按钮，点击时运行main函数
    run_button = tk.Button(window, text="运行")
    run_button.pack()

    # 创建一个返回按钮，但是默认是隐藏的
    back_button = tk.Button(window, text="返回",
                            command=lambda: back_to_main(tree, run_button, back_button, text_widget))
    back_button.pack_forget()

    # 设置运行按钮的命令
    run_button.config(command=lambda: run_main(tree, run_button, back_button, text_widget))

    window.mainloop()


def back_to_main(tree, run_button, back_button, text_widget):
    # 清空Treeview控件和滚动文本框
    for i in tree.get_children():
        tree.delete(i)
    text_widget.delete('1.0', tk.END)

    # 隐藏返回按钮，显示运行按钮
    back_button.pack_forget()
    run_button.pack()


def load_model(model_path, device):
    model = BertTextModel_last_layer().to(device)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model


def text_class_name(text, pred, args, output_file, tree):
    results = torch.argmax(pred, dim=1)
    results = results.cpu().numpy().tolist()
    classification = open(args.classification, "r", encoding="utf-8").read().split("\n")
    classification_dict = dict(zip(range(len(classification)), classification))

    with open(output_file, 'a', encoding='utf-8') as file:
        if len(results) != 1:
            for i in range(len(results)):
                file.write(f"文本：{text[i]}\t预测的类别为：{classification_dict[results[i]]}\n")
                item = tree.insert('', 'end', values=(text[i], classification_dict[results[i]]))
                # 设置每一行的背景色
                if i % 2 == 0:
                    tree.item(item, tags='evenrow')
                else:
                    tree.item(item, tags='oddrow')
        else:
            file.write(f"文本：{text}\t预测的类别为：{classification_dict[results[0]]}\n")
            item = tree.insert('', 'end', values=(text, classification_dict[results[0]]))
            tree.item(item, tags='evenrow')

<<<<<<< Updated upstream
    # 设置行的背景色
    tree.tag_configure('evenrow', background='white')
    tree.tag_configure('oddrow', background='lightgray')


def pred_from_txt(args, model, device, start, output_file, tree):
    txt_path = 'topic_230779_posts.txt'  # 替换为你的 txt 文件路径
=======
def pred_from_txt(args, model, device, start, output_file):
    txt_path = 'topic_217915_posts_2.txt'  # 替换为你的 txt 文件路径
>>>>>>> Stashed changes
    with open(txt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    texts = [line.strip().split('\t')[1] for line in lines]

    x = MyDataset(texts, labels=None, with_labels=False)
    xDataloader = DataLoader(x, batch_size=len(texts), shuffle=False)

    for batch_index, batch_con in enumerate(xDataloader):
        batch_con = tuple(p.to(device) for p in batch_con)
        pred = model(batch_con)
        text_class_name(texts, pred, args, output_file, tree)

    end = time.time()
    print(f"耗时为：{end - start} s")


if __name__ == "__main__":
    create_gui()

<<<<<<< Updated upstream
=======
    output_file = 'output_217915_2.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("模型预测结果：\n")

    pred_from_txt(args, model, device, start, output_file)

    print(f"预测结果已写入 {output_file}")
>>>>>>> Stashed changes
