import java.util.ArrayList;
import java.util.List;

public class 같은_숫자는_싫어 {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int value = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != value) {
                list.add(arr[i]);
                value = arr[i];
            }
        }

        return list.stream().mapToInt(i -> i).toArray();
    }
}
