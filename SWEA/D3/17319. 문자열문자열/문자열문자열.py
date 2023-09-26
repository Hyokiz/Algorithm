# 17319. 문자열문자열

for t in range(1, int(input()) + 1):
    n = int(input())
    s = input()
    answer = "No"
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            answer = "Yes"

    print(f'#{t} {answer}')
