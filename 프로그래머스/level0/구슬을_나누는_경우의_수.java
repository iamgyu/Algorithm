package 프로그래머스.level0;

public class 구슬을_나누는_경우의_수 {
    public int solution(int balls, int share) {
        return combination(balls, share);
    }

    public int combination(int n, int m) {
        if(m == 0 || n == m)
            return 1;
        else{
            return combination(n - 1, m - 1) + combination(n - 1, m);
        }
    }
}