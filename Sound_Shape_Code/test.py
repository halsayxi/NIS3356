import ssc
from kmp import VatiantKMP

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

ssc.getHanziStrokesDict()
ssc.getHanziStructureDict()
ssc.getHanziSSCDict()

def detect_sensitive_words(index, content):
    variabt_word = set()
    chi_word_ssc = ssc.getSSC(content, SSC_ENCODE_WAY)
    
    with open('data/filter.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            chi_word = line.strip()
            if not is_all_china(chi_word):
                continue
            chi_word_ssc_filter = ssc.getSSC(chi_word, SSC_ENCODE_WAY)
            
            kmp = VatiantKMP(SIMILARITY_THRESHOLD)
            kmp.indexKMP(chi_word_ssc, chi_word_ssc_filter, SSC_ENCODE_WAY)  # 主串S、模式串T
            
            for i in kmp.startIdxRes:
                variabt_word.add(chi_word[i:i+len(chi_word)])
    return variabt_word

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
        output_f.write("索引\t内容\t预测的类别\n")
        for line in input_f:
            index, content = line.strip().split('\t')
            variabt_word = detect_sensitive_words(index, content)
            if not variabt_word or '' in variabt_word:
                output_f.write(f"{index}\t{content}\t预测的类别为：legal\n")
            else:
                output_f.write(f"{index}\t{content}\t预测的类别为：illegal，敏感词包括：{variabt_word}\n")

if __name__ == "__main__":
    input_file = 'input/topic_217915_posts_2.txt'  # Replace with your input file path
    output_file = 'output/output_217915_2.txt'  # Replace with your desired output file path
    main(input_file, output_file)

