import sys

n = int(input())
counter = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())

    counter[num] += 1

for i in range(10001):
    if counter[i] != 0:
        for j in range(counter[i]):
            print(i)