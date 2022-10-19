function solution(s1, s2) {
    let result = 0
    for (i of s1) {
        if (s2.includes(i)) {
            result += 1;
        } else {
            continue
        }
    }
    return result
}