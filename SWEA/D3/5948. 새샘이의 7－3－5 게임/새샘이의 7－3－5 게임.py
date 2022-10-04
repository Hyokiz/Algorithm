def combinations(arr, start):
    if len(arr) == 3:
        if sum(arr) not in result:
            result.append(sum(arr))
            return

    for i in range(start, len(numbers)):
        arr.append(numbers[i])

        combinations(arr, i + 1)

        arr.pop()


for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    result = []
    combinations([], 0)
    result.sort(reverse=True)
    print(f'#{t}', result[4])