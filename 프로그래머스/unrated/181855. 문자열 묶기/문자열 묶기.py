def solution(strArr):
    li = [len(i) for i in strArr]
    return max([li.count(i) for i in range(min(li), max(li) + 1)])