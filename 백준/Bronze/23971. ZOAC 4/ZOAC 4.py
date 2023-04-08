from math import ceil

h, w, n, m = map(int, input().split())

row = ceil(h / (n + 1))
col = ceil(w / (m + 1))
print(row * col)