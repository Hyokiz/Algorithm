n, m = map(int, input().split())
buckets = list(range(n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    buckets[i], buckets[j] = buckets[j], buckets[i]

print(*buckets[1:])
