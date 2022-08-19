for t in range(1, int(input()) + 1):
    n = int(input())
    cards = list(map(str, input().split()))
    result = []
    if n % 2:
        top = cards[:n//2+1]
        bottom = cards[n//2+1:]
        for i in range(n//2):
            result.append(top[i])
            result.append(bottom[i])
        result.append(top[-1])
    else:
        top = cards[:n//2]
        bottom = cards[n//2:]
        for i in range(n//2):
            result.append(top[i])
            result.append(bottom[i])

    print(f'#{t}', end=' ')
    for i in result:
        print(i, end=' ')
    print()