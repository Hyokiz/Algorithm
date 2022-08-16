for t in range(1, int(input()) + 1):
    print(f'#{t}', end=" ")
    new_word = []
    for i in range(5):
        word = input()
        word = word + '.' * (15 - len(word))
        new_word += [word]

    result = ''
    for i in range(15):
        for j in range(5):
            result += new_word[j][i]

    print(result.replace('.', ''))