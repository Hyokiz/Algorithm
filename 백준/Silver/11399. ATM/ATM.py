n = int(input())
lines = sorted(list(map(int, input().split())))
cnt = 0

for i in range(len(lines)):
    cnt += sum(lines[:i+1])

print(cnt)