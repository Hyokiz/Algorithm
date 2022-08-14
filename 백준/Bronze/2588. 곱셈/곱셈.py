a = int(input())
b = list(map(int, input()))
cnt = 0
for i, j in enumerate(b[::-1]):
    print(a * j)
    cnt += a * j * (10 ** i)

print(cnt)