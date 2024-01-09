package 프로그래머스.level0;

import java.util.Arrays;

public class 가까운_수 {
    public int solution(int[] array, int n) {
        int answer = 0;
        Arrays.sort(array);
        int min = 100;
        for (int i : array) {
            if (min > Math.abs(i - n)) {
                min = Math.abs(i - n);
            }
        }

        for(int i : array){
            if(min == Math.abs(i - n)) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}