package 프로그래머스.level0;

public class 팩토리얼 {
    public int solution(int n) {
        int answer = 1;
        int temp = 1;
        for(int i = 1; i <= 10; i++){
            temp *= i;
            if(temp <= n) answer = i;
        }
        return answer;
    }
}