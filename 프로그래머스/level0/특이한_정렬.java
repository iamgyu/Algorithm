package 프로그래머스.level0;

import java.util.Arrays;

public class 특이한_정렬 {
    public int[] solution(int[] numlist, int n) {
        for (int i = 0; i < numlist.length - 1; i++) {
            for (int j = i + 1; j < numlist.length; j++) {
                int a = (numlist[i] - n) * (numlist[i] > n ? 1 : -1);
                int b = (numlist[j] - n) * (numlist[j] > n ? 1 : -1);
                if (a > b || (a == b && numlist[i] < numlist[j])) {
                    int temp = numlist[i];
                    numlist[i] = numlist[j];
                    numlist[j] = temp;
                }
            }
        }
        return numlist;
    }
}
