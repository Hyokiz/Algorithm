function solution(num_list) {
    var answer = [
        num_list.filter((n) => n % 2 === 0).length,
        num_list.filter((n) => n % 2 === 1).length,
    ]
    return answer
}