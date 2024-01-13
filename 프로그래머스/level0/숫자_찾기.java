package 프로그래머스.level0;

public class 숫자_찾기 {
    public int solution(int num, int k) {
        if(String.valueOf(num).contains(String.valueOf(k)))
            return String.valueOf(num).indexOf(String.valueOf(k)) + 1;
        else
            return -1;
    }
}