function solution(array, n) {
    let answer = 0;
    for (i of array) {
        if (i === n) {
            answer ++
        }
    }
    return answer
}