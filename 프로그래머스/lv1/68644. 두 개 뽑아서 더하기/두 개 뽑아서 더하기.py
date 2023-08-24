def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sums = numbers[i] + numbers[j]
            if sums not in answer:
                answer.append(sums)
    return sorted(answer) 