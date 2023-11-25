# 1024. 수열의 합

N, L = map(int, input().split())
# (x+1)+(x+2)+...+(x+n) = nx + (1+2+...+n) = nx + ((1 + n) * n) / 2 = N
# 위의 식을 x에 대해서 구한다면 x = N / n - (n + 1) / 2

for n in range(L, 101):
    x = N / n - (n + 1) / 2

    if int(x) == x: # 정수이어야 하므로 x와 int(x) 가 같다면 연속된 자연수의 합
        x = int(x)
        if x + 1 >= 0: # 양수이면 답
            for i in range(x + 1, x + n + 1):
                print(i, end=" ")

            break

else:
    print(-1)