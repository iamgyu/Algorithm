package 프로그래머스.level0;

public class 피자_나눠_먹기_3 {
    public int solution(int slice, int n) {
        return (int) Math.ceil((double) n / slice);
    }
}
