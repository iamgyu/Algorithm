package 프로그래머스.level0;

public class 게임369 {
    public int solution(int order) {
        int answer = 0;
        while(order != 0){
            int n = order % 10;
            if(n == 3 || n == 6 || n == 9)
                answer++;
            order /= 10;
        }
        return answer;
    }
}