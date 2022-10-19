function solution(arr) {
    const sum = arr.reduce((sum, x) => sum + x, 0) / arr.length
    return sum
}