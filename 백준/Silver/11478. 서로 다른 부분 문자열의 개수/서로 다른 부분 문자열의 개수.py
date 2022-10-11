# 11478. 서로 다른 부분 문자열의 개수

s = input()
arr = set()
cnt = 1
while True:
    if cnt == len(s) + 1:
        break

    for i in range(len(s)):
        arr.add(s[i:i+cnt])

    cnt += 1

print(len(arr))