package 프로그래머스.level3;

import java.util.ArrayList;
import java.util.List;

class Solution {
    private void hanoi(int n, int from, int to, List<int[]> process){
        // 종료 조건
        if(n == 1) {
            process.add(new int[] {from, to});
            return;
        }
        
        // 점화식 구현
        int empty = 6 - from - to;
        
        hanoi(n-1, from, empty, process);
        hanoi(1, from, to, process);
        hanoi(n-1, empty, to, process);
    }
    
    public int[][] solution(int n) {
        List<int[]> process = new ArrayList<>();
        hanoi(n, 1, 3, process);
        return process.toArray(new int[0][]);
    }
}