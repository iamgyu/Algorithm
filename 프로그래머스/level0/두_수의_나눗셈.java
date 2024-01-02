package 프로그래머스.level0;

public class 두_수의_나눗셈 {
    public int solution(int num1, int num2) {
        double div = (double)num1 / num2;
        return (int)(div * 1000);
    }
}
