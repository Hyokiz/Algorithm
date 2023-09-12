def solution(dartResult):
    answer = 0
    scores = list()
    curr_score = ""
    for i in dartResult:
        if i.isnumeric():
            curr_score += i
        elif i == "S":
            scores.append(int(curr_score) ** 1)
            curr_score = ""
        elif i == "D":
            scores.append(int(curr_score) ** 2)
            curr_score = ""
        elif i == "T":
            scores.append(int(curr_score) ** 3)
            curr_score = ""
        elif i == "*":
            if len(scores) > 1:
                scores[-2] *= 2
                scores[-1] *= 2
            else:
                scores[-1] *= 2
        else:
            scores[-1] *= -1
            
    return sum(scores)