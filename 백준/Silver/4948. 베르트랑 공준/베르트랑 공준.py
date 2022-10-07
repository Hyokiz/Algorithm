# 4948. 베르트랑 공준
import sys
from math import sqrt
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        if i == 1:
            continue

        elif i == 2:
            cnt += 1
            continue

        else:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break

            else:
                cnt += 1
    print(cnt)
