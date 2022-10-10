# 1181. 단어 정렬

n = int(input())
lists = list()
for _ in range(n):
    s = input()
    if s not in lists:
        lists.append(s)

lists.sort()
lists.sort(key=lambda x: len(x))

for i in lists:
    print(i)

