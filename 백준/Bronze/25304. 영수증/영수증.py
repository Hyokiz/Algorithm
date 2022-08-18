x = int(input())
n = int(input())

cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    cnt += a * b

if x == cnt:
    print("Yes")
else:
    print("No")