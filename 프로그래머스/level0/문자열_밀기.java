package 프로그래머스.level0;

public class 문자열_밀기 {
    public int solution(String A, String B) {
        int move = 100;

        if(A.equals(B))
            return 0;

        for (int i = A.length() - 1; i >= 1; i--) {
            String temp = A.substring(i) + A.substring(0, i);
            if(temp.equals(B) && move > (A.length() - i))
                move = A.length() - i;
        }

        if(move == 100)
            return -1;

        return move;
    }
}
