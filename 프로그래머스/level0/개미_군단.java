package 프로그래머스.level0;

public class 개미_군단 {
    public int solution(int hp) {
        return hp / 5 + (hp % 5) / 3 + (hp % 5 % 3);
    }
}