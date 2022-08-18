n = int(input())
number = n
cnt = 0
while True:
    a = number // 10
    b = number % 10
    number = ((a + b) % 10) + (b * 10)
    cnt += 1
    if number == n:
        break

print(cnt)