import copy
import random


# 生成棋盘
def generate(wide):
    qipan = [['*' for j in range(wide)] for i in range(wide)]
    qipanyu = [
        [
            [str(k + 1) for k in range(wide)] for j in range(wide)
        ] for i in range(wide)
    ]
    return qipan, qipanyu


# 打印棋盘
def print_chessboard(qipan):
    for i in range(len(qipan)):
        print(qipan[i])


# 修改值域
def deal_range(hang, lie, qipanyu, qipan):
    qipanyuc = qipanyu
    for i in range(len(qipanyuc)):
        if str(qipan[hang][lie]) in qipanyuc[hang][i]:
            qipanyuc[hang][i].remove(str(qipan[hang][lie]))
            if qipanyuc[hang][i] is None:
                return False
        if str(qipan[hang][lie]) in qipanyuc[i][lie]:
            qipanyuc[i][lie].remove(str(qipan[hang][lie]))
            if qipanyuc[i][lie] is None:
                return False
    # print_chessboard(qipanyu)
    return True


# 初始化棋盘
def initQ(qipan, qipanyu):
    wide = len(qipan)
    random_hang = [i for i in range(wide)]
    random_lie = [i for i in range(wide)]
    random.shuffle(random_hang)
    random.shuffle(random_lie)
    for i in range(wide):
        qipan[random_hang[i]][random_lie[i]] = str(qipanyu[random_hang[i]][random_lie[i]][random.randint(0, wide - 1)])
        deal_range(random_hang[i], random_lie[i], qipanyu, qipan)


def deal_chessboard(qipan, qipanyu, hang=0, lie=0):
    # 深度拷贝！大坑！
    qipanyuc = copy.deepcopy(qipanyu)
    qipanc = copy.deepcopy(qipan)

    if qipan[hang][lie] != '*':
        if lie < len(qipan) - 1:
            deal_chessboard(qipanc, qipanyuc, hang, lie + 1)
        else:
            if hang < len(qipan) - 1:
                deal_chessboard(qipanc, qipanyuc, hang + 1, 0)
            else:
                print_chessboard(qipan)
                exit()
    else:
        for v in qipanyuc[hang][lie].copy():
            qipanc[hang][lie] = v
            qipanyucc = copy.deepcopy(qipanyuc)
            if deal_range(hang, lie, qipanyucc, qipanc) is True:
                if lie < len(qipan) - 1:
                    deal_chessboard(qipanc, qipanyucc, hang, lie + 1)
                else:
                    if hang < len(qipan) - 1:
                        deal_chessboard(qipanc, qipanyucc, hang + 1, 0)
                    else:
                        print_chessboard(qipanc)
                        print()
                        # 为了效率，去除可获得所有解
                        exit()
            else:
                print("出现值域为空，回溯")
                continue


q, qy = generate(15)
print("生成初始棋盘：")
initQ(q, qy)

print_chessboard(q)
print("解如下：")

deal_chessboard(q, qy)
print()