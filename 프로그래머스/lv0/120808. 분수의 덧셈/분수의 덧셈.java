class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int lcm = lcm(denom1, denom2); // 두 분모의 최소공배수 구하기
        int newNumer1 = numer1 * lcm / denom1; // 최소공배수에 맞게 분자를 변환
        int newNumer2 = numer2 * lcm / denom2;
        int newNumer = newNumer1 + newNumer2; // 두 분자를 더함
        int gcd = gcd(newNumer, lcm); // 더한 분수의 분자와 분모의 최대공약수 구하기
        int[] answer = new int[2];
        answer[0] = newNumer / gcd; // 분자를 최대공약수로 나누어 기약분수로 만듦
        answer[1] = lcm / gcd; // 분모를 최대공약수로 나누어 기약분수로 만듦
        return answer;
    }
    
    // 최소공배수를 구하는 함수
    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
    
    // 최대공약수를 구하는 함수
    private int gcd(int a, int b) {
        if (a % b == 0) {
            return b;
        }
        return gcd(b, a % b);
    }
}
