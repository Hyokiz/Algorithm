for _ in range(int(input())):
    t = int(input())
    numbers = sorted(list(map(int, input().split())))
    result = [0] * 101
    for n in numbers:
        result[n] += 1

    max_value = 0
    for i in range(1, 101):
        if result[max_value] <= result[i]:
            max_value = i
    
    print(f'#{t}', max_value)
