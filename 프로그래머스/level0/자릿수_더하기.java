package 프로그래머스.level0;

public class 자릿수_더하기 {
    public int solution(int n) {
        int answer = 0;
        while (n != 0) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}