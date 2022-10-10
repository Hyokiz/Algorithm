n = int(input())
numbers = list()
for _ in range(n):
    x, y = map(int, input().split())
    numbers.append((x, y))

numbers.sort(key=lambda x: x[1])
numbers.sort()

for i in numbers:
    print(*i)