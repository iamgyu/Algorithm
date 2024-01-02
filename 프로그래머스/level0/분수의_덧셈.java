package 프로그래머스.level0;

public class 분수의_덧셈 {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        int gcd = gcd(numer, denom);

        return new int[]{numer / gcd, denom / gcd};
    }

    public int gcd(int num1, int num2) {
        if(num1 % num2 == 0)
            return num2;
        return gcd(num2, num1 % num2);
    }
}
