package 프로그래머스.level0;

public class 저주의_숫자_3 {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            answer++;
            while(answer % 3 == 0 || Integer.toString(answer).contains("3")) {
                answer++;
            }
        }
        return answer;
    }
}
