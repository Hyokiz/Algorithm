for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    number = format(m, 'b')

    if number[len(number)-n:len(number)] == '1' * n:
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')