import sys

input = sys.stdin.readline

s = str(input()).strip()
n = len(s)
answer = 1
if n % 2 == 1:
    answer = s[:n//2] == s[n//2 + 1:][::-1]
else:
    answer = s[:n//2] == s[n//2:][::-1]

if answer:
    print(1)
else:
    print(0)