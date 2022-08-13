for t in range(1, int(input()) + 1):

    numbers = list(map(int, input().split()))
    sorted_numbers = sorted(numbers)
    new_numbers = sorted_numbers[1:9]
    result = 0
    for i in new_numbers:
        result += i
    
    result = round(result/8)
    print(f'#{t} {result}')