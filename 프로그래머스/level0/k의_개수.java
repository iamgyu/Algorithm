package 프로그래머스.level0;

public class k의_개수 {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int start = i; start <= j; start++) {
            String s = Integer.toString(start);
            String compare = Integer.toString(k);
            if (s.contains(compare)) {
                answer += s.length() - s.replace(compare, "").length();
            }
        }
        return answer;
    }
}
