function solution(numbers) {
    const newNumbers = numbers.sort((a, b) => { return a - b })
    return Math.max(newNumbers[0] * newNumbers[1], newNumbers[newNumbers.length - 2] * newNumbers[newNumbers.length - 1])
}