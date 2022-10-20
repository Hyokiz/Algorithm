function solution(my_string) {
    var answer = 0;
    for (i of my_string) {
        if (Number(i)) {
            answer += Number(i);
        } else {
            continue;
        }
    }
    return answer;
}