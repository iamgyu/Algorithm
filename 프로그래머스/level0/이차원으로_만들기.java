package 프로그래머스.level0;

public class 이차원으로_만들기 {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length / n][n];
        int j = 0;
        for(int i = 0; i < num_list.length; i++){
            if(i != 0 && i % n == 0) j++;
            answer[j][i % n] = num_list[i];
        }
        return answer;
    }
}