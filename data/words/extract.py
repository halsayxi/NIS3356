# 读取txt文件
input_file_path = '敏感词库表统计.txt'
output_file_path = '敏感词库表统计_extract.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# 提取每行的最后一列
sensitive_words = [line.strip().split('\t')[-1] for line in lines]

# 写入新的txt文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word in sensitive_words:
        output_file.write(word + '\n')

print(f"Successfully extracted and saved sensitive words to {output_file_path}.")
