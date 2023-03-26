def solution(numlist, n):
    answer = []
    li = [i - n for i in numlist]
    sorted_li = sorted(li, key=lambda x: [abs(x), -x])
    for i in range(len(numlist)):
        answer.append(numlist[li.index(sorted_li[i])])
    return answer