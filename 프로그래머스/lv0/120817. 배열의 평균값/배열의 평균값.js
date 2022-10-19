function solution(numbers) {
    let sumValue = 0;
    for (i of numbers) {
        sumValue += i
    }
    return sumValue / numbers.length
}