package 프로그래머스.level0;

public class 피자_나눠_먹기_2 {
    public int solution(int n) {
        int answer = 1;
        while(answer * 6 % n != 0){
            answer++;
        }
        return answer;
    }
}
