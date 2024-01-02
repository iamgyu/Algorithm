package 프로그래머스.level0;

import java.util.Arrays;

public class 중앙값_구하기 {
    public int solution(int[] array) {
        Arrays.sort(array);
        return array[array.length / 2];
    }
}
