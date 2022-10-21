function solution(num, k) {
    const number = (''+num).split('');
    let answer = number.indexOf(k.toString())
    if (answer !== -1) {
        return answer + 1
    } else {
        return answer
    }
}