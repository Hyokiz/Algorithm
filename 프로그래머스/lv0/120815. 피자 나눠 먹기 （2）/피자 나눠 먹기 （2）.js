function solution(n) {
    let answer = n;
    while (answer % 6) {
        answer += n
    }
    return answer / 6
}