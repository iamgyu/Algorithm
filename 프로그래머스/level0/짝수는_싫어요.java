package 프로그래머스.level0;

public class 짝수는_싫어요 {
    public int[] solution(int n) {
        int arr[] = new int[(n+1) / 2];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (i + 1) * 2 - 1;
        }
        return arr;
    }
}