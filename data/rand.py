import random

with open('final6.txt','rb') as f:
    lines = f.readlines()

random.shuffle(lines)
num=len(lines)

num1=int(0.1*num)
lines1=lines[0:num1]
lines2=lines[num1+1:2*num1]
lines3=lines[2*num1+1:]

with open('./data3/test.txt', 'wb') as f:
    f.writelines(lines1)

with open('./data3/dev.txt', 'wb') as f:
    f.writelines(lines2)

with open('./data3/train.txt', 'wb') as f:
    f.writelines(lines3)