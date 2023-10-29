def solution(strArr):
    cnt = [0 for _ in range(31)]
    for i in strArr:
        cnt[len(i)] += 1
    return max(cnt)