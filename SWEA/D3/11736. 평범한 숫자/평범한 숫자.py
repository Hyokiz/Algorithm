for t in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0

    for i in range(1, n-1):
        if nums[i] == max(nums[i-1], nums[i], nums[i+1]) or nums[i] == min(nums[i-1], nums[i], nums[i+1]):
            continue
        
        ans += 1
    
    print(f'#{t}', ans)
        