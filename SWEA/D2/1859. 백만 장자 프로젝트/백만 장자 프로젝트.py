for t in range(1, int(input()) + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    result = 0

    max_value = prices[-1]
    for i in range(n-1, -1, -1):
        if prices[i] > max_value:
            max_value = prices[i]
        result += max_value - prices[i]

    print(f'#{t}', result)