def solution(score):
    answer = []
    averages = []
    for i in score:
        averages.append(sum(i))
    sorted_averages = sorted(averages, reverse=True)
    for j in averages:
        answer.append(sorted_averages.index(j) + 1)

    return answer
