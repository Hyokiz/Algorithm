for t in range(1, int(input()) + 1):
    print(f'#{t} Bob' if (int(input()) - 2) % 2 else f'#{t} Alice')