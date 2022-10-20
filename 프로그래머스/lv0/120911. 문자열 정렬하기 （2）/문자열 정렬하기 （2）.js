function solution(my_string) {
    var answer = '';
    my_string = my_string.toLowerCase();
    const li = [...my_string]
    li.sort()
    return li.join('');
}