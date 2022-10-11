# 1764. 듣보잡

n, m = map(int, input().split())
heard = set()
not_heard = set()
ans = list()
for _ in range(n):
    heard.add(input())

for _ in range(m):
    not_heard.add(input())

cnt = 0
for i in heard:
    if i not in not_heard:
        continue
    cnt += 1
    ans.append(i)

ans.sort()
print(len(ans))

for i in ans:
    print(i)

