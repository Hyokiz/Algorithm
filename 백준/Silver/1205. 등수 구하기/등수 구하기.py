# 1205. 등수 구하기

n, t, p = map(int, input().split())
if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    answer = 0
    if n == p and scores[-1] >= t:
        print(-1)
    else:
        for i in range(n):
            if t >= scores[i]:
                answer = i + 1
                break

        print(answer if answer else n + 1)