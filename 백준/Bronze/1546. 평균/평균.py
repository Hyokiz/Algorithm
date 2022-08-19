n = int(input())
scores = list(map(int, input().split()))

result = 0
for i in scores:
    result += (i * 100) / max(scores)

print(result / n)