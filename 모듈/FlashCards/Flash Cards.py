import random

t_dict = {}

while(True):
    k, v = input('문제와 정답을 입력하세요: ').split()

    if k == "exit":
        break
    t_dict[k] = "{}".format(v)

keyList = t_dict.keys()

ks = list(t_dict.keys())
random.shuffle(ks)

for kk in ks:
    vv = t_dict[kk]

    tv = input(("{}의 답은?".format(kk)))

    if tv == vv:
        print("정답!")
    else:
        print("오답!")


print(keyList)
