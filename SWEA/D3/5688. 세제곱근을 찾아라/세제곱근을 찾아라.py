for t in range(1, int(input()) + 1):
    number = int(input())
    for i in range(1, round(number ** (1/3)) + 1):
        if i ** 3 == number:
            print(f'#{t} {i}')
            break
    else:
        print(f'#{t} {-1}')
