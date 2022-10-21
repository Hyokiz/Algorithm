function solution(my_str, n) {
    var answer = [];
    const li = my_str.split('')
    let i = 0
    while (i < li.length) {
        answer.push(li.slice(i, i + n).join(''))
        i += n
    }
    return answer;
}