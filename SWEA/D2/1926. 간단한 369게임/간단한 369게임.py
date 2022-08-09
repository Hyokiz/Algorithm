n = int(input())

for i in range(1, n+1):
    i = str(i) # i를 문자열로 변환
    counts = 0
    for j in i:
        if j == '3' or j == '6' or j == '9': # i가 두자리 수 이상일 경우로 한자리씩 3, 6, 9가 포함되어 있는지 검사
            counts += 1 # 있다면 counts+1
        else:
            pass # 없으면 pass
    if counts > 0: 
        i = '-' * counts # counts 만큼 - 출력
    print(i, end=" ")