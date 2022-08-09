t = int(input())

for tc in range(1, t+1):

    words = input()
    for i in range(1, 11):
        cnt = words[:i] # i까지 슬라이싱
        cnt_next = words[i:i*2] # 같은 단어가 나올 경우 길이가 두배기 때문에 *2
        if cnt == cnt_next:
            print(f'#{tc}', i)
            break