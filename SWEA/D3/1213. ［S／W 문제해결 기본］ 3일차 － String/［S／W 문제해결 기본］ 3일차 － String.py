for _ in range(1, 11):
    t = int(input())
    word = input()
    lines = input()

    cnt = lines.count(word)
    print(f'#{t} {cnt}')