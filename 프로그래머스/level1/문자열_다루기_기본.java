public class 문자열_다루기_기본 {
    public boolean solution(String s) {
        return (s.length() == 4 || s.length() == 6) && s.replaceAll("[\\d]", "").isEmpty();
    }
}
