package 프로그래머스.level0;

public class 제곱수_판별하기 {
    public int solution(int n) {
        for (int i = 1; i < 1001; i++) {
            if(i * i == n)
                return 1;
        }
        return 2;
    }
}
