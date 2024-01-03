package 프로그래머스.level0;

import java.util.Arrays;

public class 진료_순서_정하기 {
    public int[] solution(int[] emergency) {
        int[] temp = Arrays.copyOf(emergency, emergency.length);
        int[] answer = new int[emergency.length];
        Arrays.sort(temp);
        int max = 1;
        for (int i = temp.length - 1; i >= 0; i--) {
            for (int j = 0; j < temp.length; j++) {
                if(emergency[j] == temp[i]) {
                    answer[j] = max;
                    max++;
                }
            }
        }
        return answer;
    }
}