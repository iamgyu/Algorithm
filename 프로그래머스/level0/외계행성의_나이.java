package 프로그래머스.level0;

public class 외계행성의_나이 {
    public String solution(int age) {
        String str = Integer.toString(age);
        StringBuilder answer = new StringBuilder();

        for(char c : str.toCharArray()){
            answer.append((char)((int) c + 49));
        }
        return answer.toString();
    }
}
