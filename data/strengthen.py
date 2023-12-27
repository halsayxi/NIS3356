from nlpcda import Similarword
from nlpcda import Homophone
from nlpcda import RandomDeleteChar
from nlpcda import EquivalentChar
from nlpcda import CharPositionExchange

s1 = Homophone(create_num=2, change_rate=0.3)
s2 = CharPositionExchange(create_num=2, change_rate=0.3,char_gram=3,seed=1)
s3 = EquivalentChar(create_num=2, change_rate=0.3)
s4 = Similarword(create_num=2, change_rate=0.3)

legaldata=""
illegaldata=""


with open('legal4.txt', 'r',encoding='utf-8') as f1:
  for line in f1.readlines():
    legaldata+=line

    rs1=s1.replace(line)
    rs2=s2.replace(line)
    rs3=s3.replace(line)
    rs4=s4.replace(line)

    for l in rs1:
        if '\n' not in l:
            l=l+'\n'
        if l not in legaldata:
            legaldata+=l

    for l in rs2:
        if '\n' not in l:
            l=l+'\n'
        if l not in legaldata:
            legaldata+=l

    for l in rs3:
        if '\n' not in l:
            l=l+'\n'
        if l not in legaldata:
            legaldata+=l

    for l in rs4:
        if '\n' not in l:
            l=l+'\n'
        if l not in legaldata:
            legaldata+=l

with open('legal6.txt', 'wb') as fp3:
        fp3.write(str.encode(legaldata))


with open('collectelse.txt', 'r',encoding='utf-8') as f2:
  for line in f2.readlines():
    illegaldata+=line

    rs1=s1.replace(line)
    rs2=s2.replace(line)
    rs3=s3.replace(line)
    rs4=s4.replace(line)

    for l in rs1:
        if '\n' not in l:
            l=l+'\n'
        if l not in illegaldata:
            illegaldata+=l

    for l in rs2:
        if '\n' not in l:
            l=l+'\n'
        if l not in illegaldata:
            illegaldata+=l

    for l in rs3:
        if '\n' not in l:
            l=l+'\n'
        if l not in illegaldata:
            illegaldata+=l

    for l in rs4:
        if '\n' not in l:
            l=l+'\n'
        if l not in illegaldata:
            illegaldata+=l





with open('illegal6.txt', 'wb') as fp4:
        fp4.write(str.encode(illegaldata))