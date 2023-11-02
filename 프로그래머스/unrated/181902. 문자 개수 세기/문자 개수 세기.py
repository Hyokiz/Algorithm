def solution(my_string):
    cnt = [0] * 52
    for i in my_string:
        j = ord(i)
        if j < 91:
            cnt[j - 65] += 1
        else:
            cnt[j - 71] += 1
    return cnt