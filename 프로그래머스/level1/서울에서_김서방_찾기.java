import java.util.Arrays;

public class 서울에서_김서방_찾기 {
    public String solution(String[] seoul) {
        String answer = "";
        int locate = Arrays.asList(seoul).indexOf("Kim");
        answer = "김서방은 " + locate + "에 있다";
        return answer;
    }
}
