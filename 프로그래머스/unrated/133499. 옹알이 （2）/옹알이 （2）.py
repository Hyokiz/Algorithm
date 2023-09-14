def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    repeats = ["ayaaya", "yeye", "woowoo", "mama"]
    for i in babbling:
        for repeat in repeats:
            i = i.replace(repeat, "X")
        
        for word in words:
            i = i.replace(word, "O")
        
        for j in i:
            if j != "O":
                break
        else:
            answer += 1
    return answer