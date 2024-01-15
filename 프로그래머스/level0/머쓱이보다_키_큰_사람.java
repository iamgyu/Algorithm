package 프로그래머스.level0;

public class 머쓱이보다_키_큰_사람 {
    public int solution(int[] array, int height) {
        int answer = 0;
        for(int i : array){
            if(i > height)
                answer++;
        }
        return answer;
    }
}
