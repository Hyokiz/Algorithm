import sys

n, m = map(int, sys.stdin.readline().split())

pokemon1 = {}

for i in range(1, n+1):
    pokemon1[sys.stdin.readline().rstrip()] = i

pokemon2 = {v: k for k, v in pokemon1.items()}

for _ in range(m):
    answer = sys.stdin.readline().rstrip()
    if answer.isalpha():
        print(pokemon1[answer])
    else:
        print(pokemon2[int(answer)])