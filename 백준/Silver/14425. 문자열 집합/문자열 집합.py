import sys

n, m = map(int, input().split())
string_dict = {}
for i in range(n):
    string_dict[sys.stdin.readline()] = i

cnt = 0
for j in range(m):
    check = sys.stdin.readline()
    if check in string_dict:
        cnt += 1

print(cnt)
