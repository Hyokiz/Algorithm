def solution(array):
    answer = 0
    cnt = [0] * 1000
    for i in array:
        cnt[i] += 1
    print(cnt[:10])
    # 최빈값
    max_num = max(cnt)


    if cnt.count(max_num) > 1:
        return -1
    else:
        return cnt.index(max_num)
