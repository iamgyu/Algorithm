package 프로그래머스.level0;

public class 직사각형_넓이_구하기 {
    public int solution(int[][] dots) {
        int x = 0;
        int y = 0;
        int dotX = dots[0][0];
        int dotY = dots[0][1];
        for (int i = 0; i < 4; i++) {
            if(dots[i][0] != dotX)
                x = Math.abs(dotX - dots[i][0]);
            if(dots[i][1] != dotY)
                y = Math.abs(dotY - dots[i][1]);
        }

        return x * y;
    }
}
