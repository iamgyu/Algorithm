package 프로그래머스.level0;

import java.util.Arrays;

public class 최빈값_구하기 {
    public int solution(int[] array) {
        Arrays.sort(array);
        int answer = 0;
        int max = array[array.length - 1];
        int count[] = new int[max + 1];

        for (int i = 0; i < array.length; i++) {
            count[array[i]]++;
        }

        max = count[0];
        for (int i = 1; i < count.length; i++) {
            if(max < count[i]){
                max = count[i];
                answer = i;
            } else if (max == count[i]){
                answer = -1;
            }
        }
        return answer;
    }
}