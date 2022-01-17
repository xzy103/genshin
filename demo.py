import keyboard
import pykeyboard
import time
import csv


# +号为完整一拍，-号为半拍，=号为1/4拍，*号为1/8拍，(为1/3拍，)为1/6拍，.后为节奏数
key = {'1': 'a', '2': 's', '3': 'd', '4': 'f', '5': 'g', '6': 'h', '7': 'j',
       'd': 'z', 'r': 'x', 'm': 'c', 'f': 'v', 's': 'b', 'l': 'n', 'x': 'm',
       '!': 'q', '@': 'w', '#': 'e', '$': 'r', '%': 't', '^': 'y', '&': 'u',
       '+': '+', '-': '-', '=': '=', '*': '*', '(': '(', ')': ')', '.': '.'}


# 读取乐谱
with open("score/demo.csv", 'r', encoding='utf-8') as score:
    raw_content = csv.reader(score)
    next(raw_content)  # 跳过首行
    temp = []
    for p in raw_content:
        temp.extend(p)
    temp = [i for i in temp if i != '']  # 删除列表中所有空元素


# 将乐谱中的符号转换为对应键
content = []
for i in temp:
    i = i.replace("'", "")  # #号出现在行首需要加单引号，此处解析时去除单引号
    if i.startswith('.'):
        content.append(i)
    else:
        st = ''
        for c in i:
            st += key[c]
        content.append(st)


# 调试模式
# a = '_135'
# for c in content[:]:
#     if a not in c:
#         content.remove(c)
#     else:
#         break


# 按下快捷键开始弹奏
print('按下Alt+>开始演奏')
print('按下Alt+<停止演奏')
while True:
    if keyboard.is_pressed("Alt+>"):
        break
    else:
        time.sleep(0.1)


# 对乐谱内容进行遍历
space = 0.5  # 初始化
speed = 1/1.0  # 倍数播放
for tp in content:
    exec('exit()') if keyboard.is_pressed("Alt+<") else ...  # 按下快捷键停止弹奏
    if tp.startswith('..'):
        pass
    elif tp.startswith('.'):
        space = speed * (60/int(tp[1:4]))  # 获取每拍的时长
        continue
    for e in tp:
        if e == '*':
            time.sleep(space/8)
        elif e == ')':
            time.sleep(space/6)
        elif e == '=':
            time.sleep(space/4)
        elif e == '(':
            time.sleep(space/3)
        elif e == '-':
            time.sleep(space/2)
        elif e == '+':
            time.sleep(space)
        else:
            pykeyboard.PyKeyboard().tap_key(e)
