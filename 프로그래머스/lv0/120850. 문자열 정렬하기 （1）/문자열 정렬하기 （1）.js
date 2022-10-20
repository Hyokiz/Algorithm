function solution(my_string) {
    var answer = [];
    for (i of my_string.split('')) {
        if (isNaN(i)) {
            continue
        } else {
            answer.push(Number(i))
        }
    }
    return answer.sort((a, b) => { return a - b })
}