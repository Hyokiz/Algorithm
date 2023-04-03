def solution(n):
    answer = ""
    li = [i for i in str(n)]
    li.sort(reverse=True)
    answer = "".join(li)
    return int(answer)