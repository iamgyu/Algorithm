package 프로그래머스.level3;

class Solution {
    private boolean isValid(long t, int n, int[] times){
        long c = 0;
        for(int time : times){
            c += t / time;
        }
        return c >= n;
    }
    public long solution(int n, int[] times) {
        long start = 0;
        long end = 1000000000000000000L;
        
        while (end > start) {
            long t = (start + end) / 2;
            
            // 정답 검사, 범위 좁히기
            if (isValid(t, n, times)){
                end = t;
            } else {
                start = t + 1;
            }
        }
        
        return start;
    }
}