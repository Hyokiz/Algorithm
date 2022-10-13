# 9663. N-Queen
n = int(input())

ans = 0
col = [0] * 15

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True

def dfs(x):
    global ans
    if x == n:
        ans += 1
        return

    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x+1)

dfs(0)
print(ans)