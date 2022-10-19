function solution(sides) {
    var answer = 0;
    const max = Math.max(...sides);
    return max < sides.reduce((sum, i) => sum + i, 0) - max ? 1 : 2
    
}