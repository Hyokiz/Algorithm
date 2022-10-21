n, m = map(int, input().split())
nums = list(range(1, n + 1))
def permutatations(arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        arr.append(nums[i])
        permutatations(arr)
        arr.pop()

permutatations([])