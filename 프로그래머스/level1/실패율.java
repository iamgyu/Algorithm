import java.util.HashMap;
import java.util.Map;

public class 실패율 {
    public int[] solution(int N, int[] stages) {
        Map<Integer, Double> map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            double fail = 0;
            double total = 0;
            for (int j = 0; j < stages.length; j++) {
                if(i <= stages[j]) total++;
                if(i == stages[j]) fail++;
            }
            if(fail == 0 && total == 0)
                total = 1;

            map.put(i, fail / total);
        }

        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            double max = -1;
            int m_key = 0;

            for (int key : map.keySet()) {
                if (max < map.get(key)) {
                    max = map.get(key);
                    m_key = key;
                }
            }
            answer[i] = m_key;
            map.remove(m_key);
        }

        return answer;
    }
}
