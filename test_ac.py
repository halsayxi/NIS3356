import tkinter as tk
from tkinter import ttk
import threading

# 你的代码
import Sound_Shape_Code.ssc
from Sound_Shape_Code.kmp import VatiantKMP
from crawler.output_comments import output_comments

SIMILARITY_THRESHOLD = 0.6
SSC_ENCODE_WAY = 'ALL'  # 'ALL','SOUND','SHAPE'

def make_all_china(string):
    for i in range(0, len(string)):
        if string[i] < u'\u4e00' or string[i] > u'\u9fa5':  # 判断是否是汉字，在isalpha()方法之前判断
            string.replace(string[i], '', 1)

def is_all_china(string):
    for i in range(0, len(string)):
        if string[i] < u'\u4e00' or string[i] > u'\u9fa5':  # 判断是否是汉字，在isalpha()方法之前判断
            return False
    return True

Sound_Shape_Code.ssc.getHanziStrokesDict()
Sound_Shape_Code.ssc.getHanziStructureDict()
Sound_Shape_Code.ssc.getHanziSSCDict()

def detect_sensitive_words(index, content):
    variabt_word = set()
    chi_word_ssc = Sound_Shape_Code.ssc.getSSC(content, SSC_ENCODE_WAY)

    with open('Sound_Shape_Code/data/filter.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            chi_word = line.strip()
            if not is_all_china(chi_word):
                continue
            chi_word_ssc_filter = Sound_Shape_Code.ssc.getSSC(chi_word, SSC_ENCODE_WAY)

            kmp = VatiantKMP(SIMILARITY_THRESHOLD)
            kmp.indexKMP(chi_word_ssc, chi_word_ssc_filter, SSC_ENCODE_WAY)  # 主串S、模式串T

            for i in kmp.startIdxRes:
                variabt_word.add(chi_word[i:i + len(chi_word)])
    return variabt_word

def main(topic_id):
    data = output_comments(topic_id)
    results = []
    for index, content in enumerate(data):
        variabt_word = detect_sensitive_words(index, content)
        if not variabt_word or '' in variabt_word:
            results.append((index, content, "legal", ""))
        else:
            results.append((index, content, "illegal", f"{variabt_word}"))
    return results

# tkinter UI
def run_main():
    topic_id = entry.get()
    entry.delete(0, 'end')
    results = main(topic_id)
    for index, result in enumerate(results):
        tag = 'illegalrow' if result[2] == 'illegal' else ('evenrow' if index % 2 == 0 else 'oddrow')
        tree.insert('', 'end', values=result, tags=(tag,))
    submit_button['state'] = 'normal'
    back_button['state'] = 'normal'
    loading_label.pack_forget()

def submit():
    submit_button['state'] = 'disabled'
    back_button['state'] = 'disabled'
    loading_label.pack()
    threading.Thread(target=run_main).start()

def back():
    for i in tree.get_children():
        tree.delete(i)
    submit_button['state'] = 'normal'
    back_button['state'] = 'disabled'

def create_gui():
    global root, entry, submit_button, back_button, tree, loading_label
    root = tk.Tk()
    root.geometry("800x1000")
    root.title("敏感词检测")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    entry = tk.Entry(frame, width=50)
    entry.pack(side='left')

    submit_button = tk.Button(frame, text="提交", command=submit)
    submit_button.pack(side='left')

    back_button = tk.Button(root, text="返回", command=back, state='disabled')
    back_button.pack()

    columns = ("标号", "评论内容", "判决结果", "敏感词内容")
    tree = ttk.Treeview(root, columns=columns, show='headings', height=25)
    for column in columns:
        tree.heading(column, text=column)
    tree.tag_configure('evenrow', background='white')
    tree.tag_configure('oddrow', background='lightgray')
    tree.tag_configure('illegalrow', background='lightcoral')
    tree.pack()

    loading_label = tk.Label(root, text="正在读取中...")

    root.mainloop()

if __name__ == "__main__":
    create_gui()
