package 프로그래머스.level0;

public class 이진수_더하기 {
    public String solution(String bin1, String bin2) {
        int b1 = Integer.parseInt(bin1, 2);
        int b2 = Integer.parseInt(bin2, 2);

        return Integer.toBinaryString(b1 + b2);
    }
}
