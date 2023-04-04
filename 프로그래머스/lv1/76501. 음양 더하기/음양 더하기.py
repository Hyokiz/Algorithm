def solution(absolutes, signs):
    n = len(absolutes)
    for i in range(n):
        if signs[i] == False:
            absolutes[i] *= -1
    answer = sum(absolutes)
    return answer