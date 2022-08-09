N = input()
scores = list(map(int, input().split()))
scores.sort()
print(scores[(len(scores)-1)//2])