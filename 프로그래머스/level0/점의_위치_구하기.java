package 프로그래머스.level0;

public class 점의_위치_구하기 {
    public int solution(int[] dot) {
        if(dot[0] > 0 && dot[1] > 0) return 1;
        else if(dot[0] < 0 && dot[1] > 0) return 2;
        else if(dot[0] < 0 && dot[1] < 0) return 3;
        else return 4;
    }
}