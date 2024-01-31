public class 크기가_작은_부분_문자열 {
    public int solution(String t, String p) {
        int answer = 0;
        for (int i = 0; i < t.length() - p.length() + 1; i++) {
            String temp = t.substring(i, i + p.length());
            if(Long.parseLong(temp) <= Long.parseLong(p))
                answer++;
        }

        return answer;
    }
}
