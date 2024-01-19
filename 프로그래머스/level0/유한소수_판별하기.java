package 프로그래머스.level0;

public class 유한소수_판별하기 {
    public int solution(int a, int b) {
        int gcd = 1;
        for (int i = Math.min(a, b); i > 0; i--) {
            if(a % i == 0 && b % i == 0) {
                gcd = i;
                break;
            }
        }
        b /= gcd;

        while(b % 2 == 0)
            b /= 2;
        while(b % 5 == 0)
            b /= 5;
        if(b == 1)
            return 1;
        else
            return 2;
    }
}
