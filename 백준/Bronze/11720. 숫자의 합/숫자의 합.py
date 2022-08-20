n = int(input())
n_list = list(map(int, input()))

cnt = 0
for i in range(n):
    cnt += n_list[i]

print(cnt)