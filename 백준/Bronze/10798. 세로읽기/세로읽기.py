# 10789. 세로읽기

# 최대 길이 15인, 5줄로 구성된 2차원 리스트를 만들어준다.
li = [["" for _ in range(15)] for _ in range(5)]

# 배열의 알맞은 위치에 추가해준다.
for i in range(5):
    strings = list(input())
    for j in range(len(strings)):
        li[i][j] = strings[j]

# res에 모든 결과 추가
res = ""
for r in range(15):
    for c in range(5):
        res += li[c][r]

print(res)