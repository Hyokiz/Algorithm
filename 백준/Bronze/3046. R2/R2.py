# 3046. R2

n, m = map(int, input().split())
diff = abs(n - m)
res = 0
if n < m:
    res = m + diff
else:
    res = m - diff

print(res)