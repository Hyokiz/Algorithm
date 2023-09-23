# 1003. 피보나치 함수

for _ in range(int(input())):
    n = int(input())
    zero, one = 1, 0
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)