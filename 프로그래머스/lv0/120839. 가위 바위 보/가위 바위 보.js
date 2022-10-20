function solution(rsp) {
    let answer = '';
    const cnt = rsp.split('')
    for (i of cnt) {
        if (i === '2') {
            answer += '0'
        } else if (i === '0') {
            answer += '5'
        } else {
            answer += '2'
        }
    }
    return answer
}