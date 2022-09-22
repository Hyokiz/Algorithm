n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

s, e = 0, arr[0][1]
cnt = 1
for i in arr[1:]:
    if e <= i[0]:
        s, e = i[0], i[1]
        cnt += 1

print(cnt)