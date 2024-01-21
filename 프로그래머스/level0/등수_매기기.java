package 프로그래머스.level0;

import java.util.Arrays;
import java.util.Collections;

public class 등수_매기기 {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        int[] arr = new int[score.length];
        Integer[] arr2 = new Integer[score.length];

        for (int i = 0; i < score.length; i++) {
            arr[i] = score[i][0] + score[i][1];
            arr2[i] = score[i][0] + score[i][1];
        }

        Arrays.sort(arr2, Collections.reverseOrder());

        for (int i = 0; i < score.length; i++) {
            answer[i] = Arrays.asList(arr2).indexOf(arr[i]) + 1;
        }


        return answer;
    }
}
