# 수열 정렬

n = int(input())
li = list(map(int, input().split()))
sorted_li = sorted(li)

answer = []
for i in range(n):
    idx = sorted_li.index(li[i])
    answer.append(idx)
    sorted_li[idx] = -1

print(*answer)