function solution(numbers) {
    const sortList = numbers.sort((a, b) => {
        return b - a;
    })
    const answer = numbers[0] * numbers[1]
    return answer;
}