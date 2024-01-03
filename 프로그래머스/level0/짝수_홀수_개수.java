package 프로그래머스.level0;

public class 짝수_홀수_개수 {
    public int[] solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        for(int n : num_list){
            if(n % 2 == 0) even++;
            else odd++;
        }
        return new int[]{even, odd};
    }
}
