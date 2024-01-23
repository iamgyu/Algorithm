package 프로그래머스.level0;

import java.util.Arrays;

public class A로_B_만들기 {
    public int solution(String before, String after) {
        char[] arr1 = before.toCharArray();
        char[] arr2 = after.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.toString(arr1).equals(Arrays.toString(arr2)) ? 1 : 0;
    }
}
