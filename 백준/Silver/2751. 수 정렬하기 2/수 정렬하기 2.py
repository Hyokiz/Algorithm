import sys

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in numbers:
    print(i)