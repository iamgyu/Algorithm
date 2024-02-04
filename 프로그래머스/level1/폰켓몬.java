import java.util.Arrays;

public class 폰켓몬 {
    public int solution(int[] nums) {
        int answer = nums.length / 2;
        int[] arr = Arrays.stream(nums).distinct().toArray();
        if (arr.length < nums.length / 2) {
            answer = arr.length;
        }
        return answer;
    }
}
