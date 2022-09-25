n, m = map(int,input().split())
numbers = list(map(int, input().split()))
memo = [0] * (n+1)
for i in range(n):
    memo[i+1] += numbers[i] + memo[i]

for j in range(m):
    a, b = map(int, input().split())
    print(memo[b] - memo[a-1])