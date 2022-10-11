# 1269. 대칭 차집합

a, b = map(int, input().split())
list_a = set(map(int, input().split()))
list_b = set(map(int, input().split()))
ans = set()

for i in list_a:
    if i in list_b:
        ans.add(i)
    else:
        continue

print(a + b - 2 * len(ans))