n = int(input())
info = list()
for _ in range(n):
    age, name = input().split()
    info.append((int(age), name))

info.sort(key=lambda x: x[0])

for i in info:
    print(*i)