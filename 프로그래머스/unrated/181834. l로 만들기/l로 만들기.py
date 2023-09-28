def solution(myString):
    # 108, 97
    answer = ""
    for i in myString:
        if ord(i) < 109:
            answer += "l"
        else:
            answer += i
    return answer