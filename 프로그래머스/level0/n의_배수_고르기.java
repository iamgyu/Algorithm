package 프로그래머스.level0;

import java.util.ArrayList;
import java.util.List;

public class n의_배수_고르기 {
    public int[] solution(int n, int[] numlist) {
        List<Integer> list = new ArrayList<>();
        for (int i : numlist) {
            if (i % n == 0) {
                list.add(i);
            }
        }
        return list.stream().mapToInt(i->i).toArray();
    }
}