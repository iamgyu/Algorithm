package 프로그래머스.level0;

public class 순서쌍의_개수 {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)
                answer++;
        }
        return answer;
    }
}