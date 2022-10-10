# 11651. 좌표 정렬하기2

n = int(input())
numbers = list()
for _ in range(n):
    x, y = map(int, input().split())
    numbers.append((x, y))

numbers.sort()
numbers.sort(key=lambda x: x[1])

for i in numbers:
    print(*i)