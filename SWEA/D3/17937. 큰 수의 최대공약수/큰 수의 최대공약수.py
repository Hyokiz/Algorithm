# 17937. 큰 수의 최대공약수
from math import gcd

for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    answer = 0
    if a == b:
        answer = a
    else:
        answer = gcd(a, a + 1)
        for i in range(a + 1, b):
            if answer == 1:
                break
            answer = gcd(gcd, i)
    
    print(f'#{t} {answer}')