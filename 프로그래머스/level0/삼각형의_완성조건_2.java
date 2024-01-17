package 프로그래머스.level0;

public class 삼각형의_완성조건_2 {
    public int solution(int[] sides) {
        int answer = 0;
        int max = Math.max(sides[0], sides[1]);
        int min = Math.min(sides[0], sides[1]);

        for (int i = 1; i <= max; i++) {
            if(i + min > max)
                answer++;
        }
        return answer + min - 1;
    }
}
