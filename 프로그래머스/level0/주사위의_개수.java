package 프로그래머스.level0;

public class 주사위의_개수 {
    public int solution(int[] box, int n) {
        return (box[0] / n) * (box[1] / n) * (box[2] / n);
    }
}