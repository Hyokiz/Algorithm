# 2559. 수열

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
dp = [0] * (n-k+1)
dp[0] = sum(numbers[:k])
for i in range(1, n - k + 1):
    dp[i] = dp[i-1] - numbers[i-1] + numbers[i+k-1]

print(max(dp))