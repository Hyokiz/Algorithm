# 17319. 문자열문자열

for t in range(1, int(input()) + 1):
    n = int(input())
    s = input()
    answer = "Yes" if n % 2 == 0 and s[:n//2] == s[n//2:] else "No"
    print(f'#{t} {answer}')
