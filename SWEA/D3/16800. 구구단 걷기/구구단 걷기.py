# 16800. 구구단 걷기
from math import sqrt

for t in range(1, int(input()) + 1):
    n = int(input())
    a, b = 0, 0
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            a = i
            b = n // i
            break
            
    print(f'#{t} {a + b - 2}')