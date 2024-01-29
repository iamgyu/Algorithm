import java.util.ArrayList;
import java.util.List;

public class 나누어_떨어지는_숫자_배열 {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        for (int n : arr) {
            if (n % divisor == 0)
                list.add(n);
        }
        if (list.isEmpty())
            list.add(-1);

        return list.stream().sorted().mapToInt(i -> i).toArray();
    }
}
