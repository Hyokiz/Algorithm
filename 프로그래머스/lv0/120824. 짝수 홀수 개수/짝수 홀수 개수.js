function solution(num_list) {
    var answer = [];
    let odd = 0;
    let even = 0;
    for (i of num_list) {
        if (i % 2) {
            odd ++
        } else {
            even ++
        }
    }
    answer.push(even)
    answer.push(odd)
    return answer
}