package 프로그래머스.level0;

public class 다음에_올_숫자 {
    public int solution(int[] common) {
        if (common[2] - common[1] == common[1] - common[0])
            return common[common.length - 1] + common[1] - common[0];
        else {
            return common[common.length - 1] * (common[1] / common[0]);
        }
    }
}
