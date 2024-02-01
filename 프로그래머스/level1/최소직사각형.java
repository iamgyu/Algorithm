public class 최소직사각형 {
    public int solution(int[][] sizes) {
        int small_max = 0;
        int big_max = 0;
        for (int[] size : sizes) {
            int small = Math.min(size[0], size[1]);
            int big = Math.max(size[0], size[1]);
            if (small_max < small)
                small_max = small;
            if (big_max < big)
                big_max = big;
        }
        return small_max * big_max;
    }
}
