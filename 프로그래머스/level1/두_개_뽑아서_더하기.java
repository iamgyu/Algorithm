import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 두_개_뽑아서_더하기 {
    public int[] solution(int[] numbers) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (!list.contains(numbers[i] + numbers[j]))
                    list.add(numbers[i] + numbers[j]);
            }
        }
        Collections.sort(list);
        return list.stream().mapToInt(i -> i).toArray();
    }
}
