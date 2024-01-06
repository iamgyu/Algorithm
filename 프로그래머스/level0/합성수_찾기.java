package 프로그래머스.level0;

public class 합성수_찾기 {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            int temp = 0;
            for(int j = 1; j <= i; j++){
                if(i % j == 0) temp++;
            }
            if(temp >= 3) answer++;
        }
        return answer;
    }
}