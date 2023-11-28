# 1049. 기타줄

n, m = map(int, input().split())
sixes, ones = [], []
answer = 0
for _ in range(m):
    i, j = map(int, input().split())
    sixes.append(i)
    ones.append(j)

min_six, min_one = min(sixes), min(ones)
answer = min((min_six * (n // 6) + min_one * (n % 6)), (min_six * ((n // 6) + 1)), (min_one * n))
print(answer)