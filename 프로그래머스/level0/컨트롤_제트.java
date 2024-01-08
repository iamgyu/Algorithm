package 프로그래머스.level0;

public class 컨트롤_제트 {
    public int solution(String s) {
        int answer = 0;
        String[] strArr = s.split(" ");
        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i].equals("Z")) {
                answer -= Integer.parseInt(strArr[i - 1]);
            } else {
                answer += Integer.parseInt(strArr[i]);
            }
        }
        return answer;
    }
}